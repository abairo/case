from django.conf import settings
from apps.iot_actions.repository import MQTTBroker


def get_mqtt_broker():

    return MQTTBroker(
        broker=settings.MQTT_BROKER,
        port=settings.MQTT_PORT,
        user=settings.MQTT_USER,
        password=settings.MQTT_PASSWORD,
        client=settings.MQTT_CLIENT
    )
