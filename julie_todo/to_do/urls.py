from django.urls import path
from .views import BoardAPIList, BoardAPIUpdate, TodoAPIList

urlpatterns = [
    path('board/', BoardAPIList.as_view()),
    path('board/update/<int:pk>', BoardAPIUpdate.as_view()),
    path('todo-item/', TodoAPIList.as_view()),
]
