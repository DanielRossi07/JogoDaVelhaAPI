import json
from channels.generic.websocket import WebsocketConsumer


class TicTacToeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'message': 'You are now connected to the Tic Tac Toe game.'
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        self.send(text_data=json.dumps({
            'message': text_data
        }))
