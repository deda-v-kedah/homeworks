from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly

from advertisements.filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter
    search_fields = ['created_at']

    def get_permissions(self):
        
        """Получение прав для действий."""
        if self.action in ["create", "update", "destroy", "partial_update"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return [ ]
