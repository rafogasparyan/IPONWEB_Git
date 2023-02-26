import json

#
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import Customer


class CustomerView(View):

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
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            customer_data = {
                'id': customer.id,
                'customer': {
                    'id': customer.user.id,
                    'username': customer.user.username,
                    'email': customer.user.email,
                },
                'registered_at': customer.registered_at.isoformat(),
                'avatar': request.build_absolute_uri(customer.avatar.url) if customer.avatar else None,
            }
            data.append(customer_data)
        return CustomerView.data_status(data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)

        user_id = data.get('user_id')
        registered_at = timezone.now()
        avatar = data.get('avatar')

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist'}, status=400)

        customer = Customer(user=user, registered_at=registered_at, avatar=avatar)
        customer.save()
        return CustomerView.ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return CustomerView.data_status({
            "id": customer.id,
            'customer': {
                'id': customer.user.id,
                'username': customer.user.username,
                'email': customer.user.email,
            },
            'registered_at': customer.registered_at.isoformat(),
            'avatar': request.build_absolute_uri(customer.avatar.url) if customer.avatar else None,
        })

    @staticmethod
    def delete(request, id):

        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        customer.delete()
        return CustomerView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        if 'user_id' in data:
            try:
                user_id = User.objects.get(id=data['user_id'])
                customer.user = user_id
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})
        customer.save()
        return CustomerView.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)