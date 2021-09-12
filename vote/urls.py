from django.urls import path
from rest_framework import routers

from vote.views import VoteViewSet, WinnerMenu

router = routers.SimpleRouter()
router.register('', VoteViewSet, basename='vote')
urlpatterns = router.urls
urlpatterns += [
    path('winner', WinnerMenu.as_view(), name='winner')
]
