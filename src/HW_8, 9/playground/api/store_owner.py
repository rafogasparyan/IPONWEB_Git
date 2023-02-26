import json

#
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

#
from ..models import StoreOwner


class StoreOwnerView(View):

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
        owners = StoreOwner.objects.all()
        data = []
        for owner in owners:
            owner_data = {
                'id': owner.id,
                'user': {
                    'id': owner.user.id,
                    'username': owner.user.username,
                    'email': owner.user.email,
                },
                'registered_at': owner.registered_at.isoformat(),
                'avatar': request.build_absolute_uri(owner.avatar.url) if owner.avatar else None,
            }
            data.append(owner_data)
        return StoreOwnerView.data_status(data)

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

        owner = StoreOwner(user=user, registered_at=registered_at, avatar=avatar)
        owner.save()
        return StoreOwnerView.ok_status()

    @staticmethod
    def get_single(request, id):

        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return StoreOwnerView.data_status({
            "id": owner.id,
            'user': {
                'id': owner.user.id,
                'username': owner.user.username,
                'email': owner.user.email,
            },
            'registered_at': owner.registered_at.isoformat(),
            'avatar': request.build_absolute_uri(owner.avatar.url) if owner.avatar else None,
        })

    @staticmethod
    def delete(request, id):

        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        owner.delete()
        return StoreOwnerView.ok_status()

    @staticmethod
    def edit(request, id):

        data = json.loads(request.body)

        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        if 'user_id' in data:
            try:
                user_id = User.objects.get(id=data['user_id'])
                owner.user = user_id
            except ObjectDoesNotExist:
                return HttpResponse({'status': 'obj_not_found'})
        owner.save()
        return StoreOwnerView.ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)