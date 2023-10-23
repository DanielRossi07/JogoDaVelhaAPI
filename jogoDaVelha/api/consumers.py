import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .gameClasses.game import Game
from django.template.loader import render_to_string


class TicTacToeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type', '')

        if message_type == 'player_info':
            print("Player info received")
            board_template = render_to_string('api/game_board.html', context={})
            await self.load_template(board_template)
            await self.process_player_info(text_data_json)
        elif message_type == 'play':
            print("Player move received")
            await self.play(text_data_json)

    async def process_player_info(self, data):
        player_name = data.get('playerName', '')
        player_type = data.get('playerType', '')

        print("Creating game")
        self.game = Game(player_name, player_type, self)

    async def play(self, data):
        move_row = data.get('row', '')
        move_col = data.get('col', '')
        await self.game.make_a_move(move_row, move_col)

    async def load_template(self, template):
        await self.send(text_data=json.dumps({
            'type': 'load_template',
            'template': template,
        }))
