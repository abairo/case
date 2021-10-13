from rest_framework.viewsets import ReadOnlyModelViewSet, mixins, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import IOTActionsSerializer, IOTEventSerializer
from .models import IOTAction, IOTEvent


class IOTActionViewSet(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IOTActionsSerializer
    queryset = IOTAction.objects.all()

    def get_queryset(self):
        return self.queryset.filter(active=True)


class IOTEventViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IOTEventSerializer
    queryset = IOTEvent.objects.all()
