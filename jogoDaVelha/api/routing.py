from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r'ws/tic-tac-toe-game/', consumers.TicTacToeConsumer.as_asgi()),
]