from rest_framework import serializers

from restaurant.models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return super().create(validated_data)

    class Meta:
        model = Restaurant
        fields = ("id", "name", "owner")
        extra_kwargs = {"owner": {"write_only": True}}

