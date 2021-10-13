from rest_framework import serializers
from .models import IOTAction, IOTEvent


class IOTActionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTAction
        fields = ('id', 'name', 'description')


class IOTEventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = IOTEvent
        fields = ('id', 'iot_action', 'value', 'user')
