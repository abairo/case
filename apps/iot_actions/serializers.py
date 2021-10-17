from rest_framework import serializers
from .models import IOTAction, IOTEvent
from .usecases import PublishTopic
from .repository import MQTTBroker


class IOTActionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = IOTAction
        fields = ('id', 'name', 'description')


class IOTEventSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = IOTEvent
        fields = ('id', 'iot_action', 'value', 'user', 'created_at')

    def save(self, *args, **kwargs):
        validated_data = self.validated_data
        topic = validated_data['iot_action'].topic
        value = validated_data['value']
        usecase = PublishTopic(MQTTBroker())

        usecase(topic, value)
        super(IOTEventSerializer, self).save(*args, **kwargs)
