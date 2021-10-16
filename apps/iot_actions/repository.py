from paho.mqtt import client as paho


class MQTTBroker():

    __slots__ = ('_broker', '_port', '_user',
                 '_password', '_client_name',)

    def __init__(self, broker, port, user, password, client):
        self._broker = broker
        self._port = port
        self._user = user
        self._password = password
        self._client_name = client

    def publish_message(self, topic, message):
        try:
            client1= paho.Client(self._client_name)
            client1.on_publish = lambda x, y, z: (x, y, z)
            client1.username_pw_set(username=self._user, password=self._password)
            client1.connect(self._broker, self._port, 60)
            ret = client1.publish(topic, payload=message)
        #TODO create connection class and implement context manager to close connection
        finally:
            client1.disconnect()


if __name__ == '__main__':
    from decouple import config
    broker = config('MQTT_BROKER')
    port = config('MQTT_PORT', cast=int)
    user = config('MQTT_USER')
    password = config('MQTT_PASSWORD')
    client = config('MQTT_CLIENT')
    mqtt_broker = MQTTBroker(broker, port, user, password, client)
    mqtt_broker.publish_message('teste', 1)

