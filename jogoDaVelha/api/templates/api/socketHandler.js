const gameAPI = {
    socket: new WebSocket(`ws://${window.location.host}/ws/tic-tac-toe-game/`),
};

document.addEventListener("DOMContentLoaded", function () {
	gameAPI.socket.onopen = function (event) {
		console.log("WebSocket connected.")
	}

    gameAPI.socket.onmessage = function (event) {
        var template_body = document.getElementById('template_body');
        var serverMessage = JSON.parse(event.data);
        console.log(serverMessage);

        if (serverMessage.type == "gamestatus"){
            updateBoard(serverMessage);
        }else{
			template_body.innerHTML = serverMessage.template;
		}

    };

    gameAPI.socket.onclose = function (event) {
        console.log("WebSocket connection closed.");
    };

	function getPlayerInfo(event){
		var playerName = document.getElementById('playerName').value;
		var playerType = document.getElementById('playerType').value;

		var playerInfo = JSON.stringify({
			'type': "player_info",
			'playerName': playerName,
			'playerType': playerType
		});

		gameAPI.socket.send(playerInfo);
	}

	function getPlayerMove(event){
		var clicked_square = event.target.dataset;

		var row = clicked_square.row;
		var col = clicked_square.col;

		var playerMove = JSON.stringify({
			'type': "play",
			'row': row,
			'col': col
		});

		gameAPI.socket.send(playerMove);
	}

	function updateBoard(serverMessage){
		var row = serverMessage.current_move_row;
		var col = serverMessage.current_move_col;
		var playerType = serverMessage.player_type;

		var board_square = document.querySelector(`[data-position="${row}, ${col}"]`);
		if (board_square){
			board_square.textContent = playerType;
		}
	}
});