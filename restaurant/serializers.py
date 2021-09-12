from rest_framework import serializers

from account.serializers import UserSerializer
from restaurant.models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ("id", "name", "owner")
        extra_kwargs = {"owner": {"write_only": True}}


class ReadMenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()

    class Meta:
        model = Menu
        fields = ("id", "restaurant", "name", "details", "vote_count")
        read_only_fields = fields


class WriteMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ("id", "restaurant", "name", "details")
        extra_kwargs = {"restaurant": {"write_only": True},
                        "serving_date": {"read_only": True}}
