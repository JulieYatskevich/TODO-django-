from celery import shared_task

from .models import Board


@shared_task
def change_board_status():
    Board.objects.update(completed=True)
