from abc import ABC

from . import models
from rest_framework import serializers


class result_serializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        title = None
        result_code = None
        try:
            title = data.title
            result_code = data.result_code
        except Exception as a:
            print('empty fields ' + str(a))
        # Perform the data validation.
        if title is None:
            raise serializers.ValidationError({
                'title': 'This field is required.'
            })
        if result_code is None:
            raise serializers.ValidationError({
                'result_code': 'This field is required.'
            })

        return {
            'title': title,
            'result_code': result_code
        }

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def to_representation(self, instance):
        return {
            'title': instance['title'],
            'result_code': instance['result_code']
        }


class user_serializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['read_ison']:
            self.fields['phone_number'].read_only = True
            self.fields['key'].read_only = True
        else:
            self.fields['phone_number'].write_only = True
            self.fields['key'].write_only = True

    class Meta:
        model = models.user_model
        fields = ['phone_number',
                  'key',
                  'username',
                  'password',
                  'url',
                  'created_at',
                  'created_by',
                  'had_bought',
                  'customer_code',
                  'introducer_code']

    def save(self, **kwargs):
            user = models.user_model.objects.get(phone_number=self.data['phone_number'])
            user.username = self.data['username']
            user.key = self.data['key']
            user.password = self.data['password']
            user.url = self.data['url']

            user.save(update_fields=['username', 'key', 'password', 'url'])


class error_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.error_model
        fields = ('ip', 'log')
