from django.utils import timezone
from rest_framework import generics, permissions

from .models import Board, TodoItem
from .serializers import BoardSerializer, TodoItemSerializer

date = timezone.localdate()


class BoardAPIList(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        date = timezone.localdate()
        return super().get_queryset().filter(user=user, start=date)


class BoardAPIUpdate(generics.UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)


class TodoAPIList(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     status = self.request.status
    #     return super().get_queryset().filter(status=status)
