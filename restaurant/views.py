import datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from account.models import UserType
from restaurant.models import Restaurant, Menu
from restaurant.permissions import IsOwnerOrReadOnly
from restaurant.serializers import RestaurantSerializer, ReadMenuSerializer, WriteMenuSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_types == UserType.OWNER:
                return Restaurant.objects.select_related('owner').filter(owner=self.request.user)
            else:
                return Restaurant.objects.select_related('owner').all()
        else:
            return Restaurant.objects.all()


class MenuViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.user_types == UserType.OWNER:
                return Menu.objects.select_related('restaurant').filter(restaurant__owner=self.request.user)
            elif self.request.user.user_types == UserType.EMPLOYEE:
                return Menu.objects.select_related('restaurant').filter(serving_date=datetime.datetime.today)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadMenuSerializer
        return WriteMenuSerializer
