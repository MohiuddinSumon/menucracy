from rest_framework import viewsets

from account.models import UserType
from restaurant.models import Restaurant
from restaurant.permissions import IsOwnerOrReadOnly
from restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_types == UserType.OWNER:
                return Restaurant.objects.select_related('owner').filter(owner=self.request.user)
            else:
                return Restaurant.objects.select_related('owner').all()
        else:
            return Restaurant.objects.all()

