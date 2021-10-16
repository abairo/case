class PublishTopic():

    __slots__ = ('_broker_mqtt',)

    def __init__(self, broker_mqtt):
        self._broker_mqtt = broker_mqtt

    def _publish_message(self, topic, value):
        return self._broker_mqtt.publish_message(topic, value)

    def __call__(self, topic: str, value: int):
        return self._publish_message(topic, value)
