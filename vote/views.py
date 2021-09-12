from datetime import date
from datetime import timedelta

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

from restaurant.models import Menu, Restaurant
from restaurant.serializers import ReadMenuSerializer
from vote.serializers import VoteSerializer


class VoteViewSet(ModelViewSet):
    serializer_class = VoteSerializer
    http_method_names = ['get', 'post']


class WinnerMenu(APIView):

    @staticmethod
    def get_winner(day):
        return Menu.objects.select_related('restaurant').filter(serving_date=day).order_by('-vote_count').first()

    def get(self, request):

        today = date.today()
        yesterday = today - timedelta(days=1)
        day_before_yesterday = today - timedelta(days=2)

        winner = self.get_winner(today)

        if Restaurant.objects.count() > 1:
            yesterday_winner = self.get_winner(yesterday)
            day_before_yesterday_winner = self.get_winner(day_before_yesterday)

            if winner and yesterday_winner and day_before_yesterday_winner:
                if winner.restaurant == yesterday_winner.restaurant == day_before_yesterday_winner.restaurant:
                    second_winner = Menu.objects.select_related('restaurant').filter(serving_date=today).order_by('-vote_count')[1]
                    serializer = ReadMenuSerializer(second_winner)
                    return Response(serializer.data)

        serializer = ReadMenuSerializer(winner)
        return Response(serializer.data)
