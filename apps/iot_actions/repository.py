from paho.mqtt import client as paho
from django.conf import settings


class MQTTBroker():

    __slots__ = ()

    def publish_message(self, topic, message):
        client = settings.MQTT
        print(f'Conectado: {client.is_connected()}')
        if not client.is_connected():
            print('reconectando...')
            client.reconnect()
        ret = client.publish(topic, payload=message)
        print(f'retorno: {ret}')


if __name__ == '__main__':
    from decouple import config
    broker = config('MQTT_BROKER')
    port = config('MQTT_PORT', cast=int)
    user = config('MQTT_USER')
    password = config('MQTT_PASSWORD')
    client = config('MQTT_CLIENT')
    mqtt_broker = MQTTBroker(broker, port, user, password, client)
    mqtt_broker.publish_message('teste', 1)

