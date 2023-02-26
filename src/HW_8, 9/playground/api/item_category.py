import json

#
from django.http import HttpResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import ItemCategory


class ItemCategoryView(View):

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
        categories = ItemCategory.objects.all()
        print(categories)
        data = []
        for category in categories:
            category_data = {
                'id': category.id,
                'name': category.name,
                'picture': request.build_absolute_uri(category.picture.url) if category.picture else None,
            }
            data.append(category_data)
        return ItemCategoryView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        category = ItemCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ItemCategoryView.ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return ItemCategoryView.data_status({
            "id": category.id,
            "name": category.name,
            'picture': request.build_absolute_uri(category.picture.url) if category.picture else None,
        })

    @staticmethod
    def delete(request, id):

        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        category.delete()
        return ItemCategoryView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            category = ItemCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return ItemCategoryView.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemCategoryView.edit(request, id)