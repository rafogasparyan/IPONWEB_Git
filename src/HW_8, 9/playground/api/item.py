import json

#
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import Item, ItemCategory, Store


class ItemView(View):

    @staticmethod
    def data_status(data):
        return HttpResponse(
            json.dumps(data),
            status=200,
            content_type='application/json',
        )

    @staticmethod
    def ok_status():
        return HttpResponse(
            json.dumps({"status": "ok"}), status=200, content_type="application/json"
        )

    @staticmethod
    def get(request):
        items = Item.objects.all()
        data = []
        for item in items:
            item_data = {
                'id': item.id,
                'name': item.name,
                'picture': request.build_absolute_uri(item.picture.url) if item.picture else None,
                'item_category': item.category.name,
                'price': item.price,
                'quantity': item.quantity,
                'description': item.description,
                'store': item.store.name,
            }
            data.append(item_data)
        return ItemView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)

        name = data.get('name')
        picture = data.get('picture')
        category_id = data.get('category_id')
        price = data.get('price')
        quantity = data.get('quantity')
        description = data.get('description')
        store_id = data.get('store_id')

        try:
            category = ItemCategory.objects.get(id=category_id)
            store = Store.objects.get(id=store_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Object does not exist'}, status=400)

        item = Item.objects.create(
            name=name,
            picture=picture,
            category=category,
            price=price,
            quantity=quantity,
            description=description,
            store=store,
        )
        item.save()
        return ItemView.ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemView.data_status({
            'id': item.id,
            'name': item.name,
            'picture': request.build_absolute_uri(item.picture.url) if item.picture else None,
            'item_category': item.category.name,
            'price': item.price,
            'quantity': item.quantity,
            'description': item.description,
            'store': item.store.name,
        })

    @staticmethod
    def delete(request, id):

        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        item.delete()
        return ItemView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        if 'name' in data:
            try:
                item.name = data['name']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'picture' in data:
            try:
                item.picture = data['picture']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'category_id' in data:
            try:
                category = ItemCategory.objects.get(id=data['category_id'])
                item.category = category
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'price' in data:
            try:
                item.price = data['price']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'quantity' in data:
            try:
                item.quantity = data['quantity']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'description' in data:
            try:
                item.description = data['description']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'store_id' in data:
            try:
                store = Store.objects.get(id=data['store_id'])
                item.store = store
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        item.save()
        return ItemView.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)