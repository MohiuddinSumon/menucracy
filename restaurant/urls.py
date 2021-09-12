from restaurant.views import RestaurantViewSet, MenuViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register("menus", MenuViewSet, basename="menu")
router.register("", RestaurantViewSet, basename="restaurant")
urlpatterns = router.urls
