import json
from channels.generic.websocket import WebsocketConsumer
from .gameClasses.game import Game


class TicTacToeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type', '')

        if message_type == 'player_info':
            self.process_player_info(text_data_json)
        elif message_type == 'play':
            self.play(text_data_json)

    def process_player_info(self, data):
        player_name = data.get('playerName', '')
        player_type = data.get('playerType', '')

        self.game = Game()
        self.game.create_player(player_name, player_type, self)
        self.game.start()

    def play(self, data):
        move_row = data.get('moveRow', '')
        move_col = data.get('moveCol', '')
        self.game.player.make_a_move(move_row, move_col)
