from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

class AbstractViewSet(ModelViewSet):
    filter_backends = [OrderingFilter]
    ordering_fields = ["updated", "created"]
    ordering = ["-updated"]