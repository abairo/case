from django.db import models
from django.contrib.auth import get_user_model
import uuid


USER = get_user_model()


class CaseIOTBase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class IOTAction(CaseIOTBase):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    topic = models.CharField(max_length=200)
    active = models.BooleanField(default=False)


class IOTEvent(CaseIOTBase):
    SENT = 'SENT'
    FAILED = 'FAILED'
    UNDEFINED = 'UNDEFINED'
    EVENT_STATUS_CHOICES = (
        (SENT, 'Message sent'),
        (FAILED, 'Failed'),
        (UNDEFINED, 'Undefined')
    )

    iot_action = models.ForeignKey(IOTAction, on_delete=models.PROTECT)
    status = models.CharField(choices=EVENT_STATUS_CHOICES, default=UNDEFINED,
                              max_length=20)
    value = models.SmallIntegerField()
    user = models.ForeignKey(USER, on_delete=models.PROTECT)
