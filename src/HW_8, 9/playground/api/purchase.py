import json

#
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic import View

#
from ..models import Item, Customer, Purchase


class PurchaseView(View):

    @staticmethod
    def calculate_total_sum(purchase):
        total_price = 0
        for item in purchase.items.all():
            total_price += item.price
        purchase.total_price = total_price

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
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            purchase_data = {
                "purchase_id": purchase.id,
                "customer": purchase.customer.user.username,
                "buy_time": purchase.buy_time.isoformat(),
                "items": [
                    {
                        "id": item.id,
                        "name": item.name,
                        "price": item.price,
                        "description": item.description
                    } for item in purchase.items.all()
                ],
                "total_price": purchase.total_price,
            }
            data.append(purchase_data)
        return PurchaseView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=data['customer_id'])
            items = data.get('items')

            purchase = Purchase.objects.create(customer=customer)
            purchase.save()
            for item_id in items:
                item = Item.objects.get(id=item_id)
                purchase.items.add(item)
            PurchaseView.calculate_total_sum(purchase)
            purchase.save()

            return PurchaseView.ok_status()
        except ObjectDoesNotExist:
            return HttpResponse("Invalid data", status=400)

    @staticmethod
    def get_single(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        return PurchaseView.data_status({
            "customer": purchase.customer.user.username,
            "buy_time": purchase.buy_time.isoformat(),
            "items": [
                {
                    "id": item.id,
                    "name": item.name,
                    "price": item.price,
                    "description": item.description
                } for item in purchase.items.all()
            ],
            "total_price": purchase.total_price,
        })

    @staticmethod
    def delete(request, id):

        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        purchase.delete()
        return PurchaseView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            purchase = Purchase.objects.get(id=id)

            if "customer_id" in data:
                purchase.customer = Customer.objects.get(id=data['customer_id'])
            if "items" in data:
                purchase.items.set([Item.objects.get(id=item_id) for item_id in data['items']])
            PurchaseView.calculate_total_sum(purchase)

            purchase.save()

            return PurchaseView.ok_status()
        except ObjectDoesNotExist:
            return HttpResponse({'status': 'obj_not_found'})

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)