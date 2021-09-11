from restaurant.views import RestaurantViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register("", RestaurantViewSet, basename="restaurant")
urlpatterns = router.urls
