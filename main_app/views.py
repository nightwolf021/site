from _dbus_bindings import Dictionary
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import user_serializer, result_serializer, error_serializer
from .models import user_model, result_model, error_model


class update_key(APIView):
    def post(self, request):
        request_serialized = user_serializer(context=({'read_ison': False}), data=request.data)
        request_serialized.is_valid()
        try:
            request_phone_number = request.data['phone_number']
        except Exception as e:
            print('request_phone_number is empty ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='phone_needed'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_400_BAD_REQUEST)
        try:
            request_key = request.data['key']
        except Exception as e:
            print('request_key is empty ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='key_needed'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_400_BAD_REQUEST)
        try:
            saved_user = user_model.objects.get(phone_number=request_phone_number)
            request_serialized.update(saved_user, request.data)
            return Response(request_serialized.data)
        except Exception as e:
            print('error while finding user ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='user_not_found'))
            result_serialized.is_valid()
            return Response(result_serialized.data, status=status.HTTP_404_NOT_FOUND)


class key_isvalid(APIView):
    def post(self, request):
        request_serialized = user_serializer(context={'read_ison': False}, data=request.data)
        request_serialized.is_valid()
        try:
            request_phone_number = request.data['phone_number']
        except Exception as e:
            print('request_phone_number is empty ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='phone_needed'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_400_BAD_REQUEST)
        try:
            request_key = request.data['key']
        except Exception as e:
            print('request_key is empty ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='key_needed'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_400_BAD_REQUEST)
        try:
            saved_user = user_model.objects.get(phone_number=request_phone_number)
        except Exception as e:
            print("user not found " + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='user_not_found'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_404_NOT_FOUND)
        if getattr(saved_user, 'key') == request_key:
            result_serialized = result_serializer(data=result_model.objects.get(label='key_valid'))
        else:
            result_serialized = result_serializer(data=result_model.objects.get(label='key_invalid'))
        result_serialized.is_valid()
        print(result_serialized.errors)
        print(result_serialized.is_valid())

        return Response(data=result_serialized.data, status=status.HTTP_200_OK)


class make_log(APIView):
    def post(self, request):
        serilized_error = error_serializer(data=request.data)
        serilized_error.is_valid()
        try:
            request_log = request.data['log']
            serilized_error.save()
            result_serialized = result_serializer(data=result_model.objects.get(label='done'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print('log is empty ' + str(e))
            result_serialized = result_serializer(data=result_model.objects.get(label='log_isneeded'))
            result_serialized.is_valid()
            return Response(data=result_serialized.data, status=status.HTTP_400_BAD_REQUEST)
