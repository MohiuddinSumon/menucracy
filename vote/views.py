from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from restaurant.models import Menu
from restaurant.serializers import ReadMenuSerializer
from vote.serializers import VoteSerializer


class VoteViewSet(ModelViewSet):
    serializer_class = VoteSerializer


class WinnerMenu(APIView):

    def get(self, request):
        menu = Menu.objects.select_related('restaurant').all().order_by('-vote_count').first()

        serializer = ReadMenuSerializer(menu)
        return Response(serializer.data)
