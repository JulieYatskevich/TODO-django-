from django.db import transaction
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, response, status
from rest_framework.decorators import action

from to_do.tasks import change_board_status

from .models import Board, TodoItem
from .serializers import BoardSerializer, TodoItemSerializer

date = timezone.localdate()


class BoardAPIList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        date = timezone.localdate()
        return super().get_queryset().filter(user=user, start=date)

    @transaction.atomic
    @action(
        detail=False,
        methods=['post'],
        url_path='change-board-status',
    )
    def change_status(self, request):
        change_board_status.apply_async(kwargs={'completed': False})
        return response.Response(status=status.HTTP_20_OK)


class BoardAPIUpdate(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)


class TodoAPIList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
