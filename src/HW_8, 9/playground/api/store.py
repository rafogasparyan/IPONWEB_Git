import json

#
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import Store, StoreCategory, StoreOwner


class StoreView(View):

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
        stores = Store.objects.all()
        data = []
        for store in stores:
            store_data = {
                'id': store.id,
                'store_category': store.store_category.name,
                'name': store.name,
                'owner': {
                    'owner_id': store.owner.id,
                    'user_id': store.owner.user.id,
                    'username': store.owner.user.username,
                    'email': store.owner.user.email,
                },
            }
            data.append(store_data)
        return StoreView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)

        category_id = data.get('category_id')
        name = data.get('name')
        owner_id = data.get('owner_id')

        try:
            category = StoreCategory.objects.get(id=category_id)
            owner = StoreOwner.objects.get(id=owner_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Object does not exist'}, status=400)

        store = Store(store_category=category, name=name, owner=owner)
        store.save()
        return StoreView.ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreView.data_status({
            'id': store.id,
            'store_category': store.store_category.name,
            'name': store.name,
            'owner': {
                'owner_id': store.owner.id,
                'user_id': store.owner.user.id,
                'username': store.owner.user.username,
                'email': store.owner.user.email,
            }})

    @staticmethod
    def delete(request, id):

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        store.delete()
        return StoreView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        if 'category_id' in data:
            try:
                category = StoreCategory.objects.get(id=data['category_id'])
                store.store_category = category
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'name' in data:
            try:
                store.name = data['name']
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        if 'owner_id' in data:
            try:
                owner = StoreOwner.objects.get(id=data['owner_id'])
                store.owner = owner
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})

        store.save()
        return StoreView.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.delete(request, id)
        if request.method == "PATCH":
            return StoreView.edit(request, id)