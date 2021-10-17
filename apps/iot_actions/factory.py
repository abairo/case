from django.conf import settings
from apps.iot_actions.repository import MQTTBroker
from paho.mqtt import client as paho


def mqtt_broker():
    broker=settings.MQTT_BROKER
    port=settings.MQTT_PORT
    user=settings.MQTT_USER
    password=settings.MQTT_PASSWORD
    client=settings.MQTT_CLIENT

    client = paho.Client(client)
    client.on_publish = lambda x, y, z: (x, y, z)
    client.username_pw_set(username=user, password=password)
    client.connect(broker, port, 60)
    client.loop_start()

    return client
