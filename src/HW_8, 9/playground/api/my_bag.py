import json

#
from django.http import HttpResponse
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import Item, Customer, MyBag


class MyBagView(View):

    @staticmethod
    def calculate_total_sum(mybag):
        total_price = 0
        for item in mybag.items.all():
            total_price += item.price
        mybag.total_price = total_price

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
        bags = MyBag.objects.all()
        data = []
        for mybag in bags:
            bag_data = {
                "bag_id": mybag.id,
                "customer": mybag.customer.user.username,
                "items": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "price": item.price,
                        "description": item.description
                    } for item in mybag.items.all()
                ],
                "total_price": mybag.total_price,
            }
            data.append(bag_data)
        return MyBagView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=data['customer_id'])
            items = data.get('items')

            mybag = MyBag.objects.create(customer=customer)
            mybag.save()
            for item_id in items:
                item = Item.objects.get(id=item_id)
                mybag.items.add(item)
            MyBagView.calculate_total_sum(mybag)
            mybag.save()

            return MyBagView.ok_status()
        except ObjectDoesNotExist:
            return HttpResponse("Invalid data", status=400)

    @staticmethod
    def get_single(request, id):
        try:
            mybag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        return MyBagView.data_status({
            "customer_id": mybag.customer.id,
            "items": [
                {
                    "id": item.id,
                    "name": item.name,
                    "price": item.price,
                    "description": item.description
                } for item in mybag.items.all()
            ],
            "total_price": mybag.total_price
        })

    @staticmethod
    def delete(request, id):

        try:
            mybag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        mybag.delete()
        return MyBagView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            mybag = MyBag.objects.get(id=id)

            if "customer_id" in data:
                mybag.customer = Customer.objects.get(id=data['customer_id'])
            if "items" in data:
                mybag.items.set([Item.objects.get(id=item_id) for item_id in data['items']])
            MyBagView.calculate_total_sum(mybag)

            mybag.save()

            return MyBagView.ok_status()
        except ObjectDoesNotExist:
            return HttpResponse({'status': 'obj_not_found'})

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)
