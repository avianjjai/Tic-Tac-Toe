import pickle
from Board import Board
from Player import Player
from Constants import WIN, LOSS, TIE, PLAY

class Game:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.board = Board()
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_1.piece = 'X'
        self.player_2.piece = 'O'
        self.winner = None
        self.losser = None
        self.__TURN = True

    def __next_move(self):
        if self.__TURN:
            self.winner, self.looser = [self.player_1, self.player_2] if self.player_1.play(self.board) else [None, None]
        else:
            self.winner, self.looser = [self.player_2, self.player_1] if self.player_2.play(self.board) else [None, None]


        if self.winner:
            self.winner.game_status = WIN
            self.looser.game_status = LOSS

        self.__TURN = not self.__TURN
        
    def HandShake(self):
        send = pickle.dumps({'type': 'HAND SACK', 'piece': self.player_1.piece})
        self.player_1.pointer.send(send)

        send = pickle.dumps({'type': 'HAND SACK', 'piece': self.player_2.piece})
        self.player_2.pointer.send(send)

    def start_Game(self):
        self.HandShake()

        while not self.board.endGame():
            self.__next_move()
            if self.winner:
                break

        if not self.winner:
            self.player_1.game_status = TIE
            self.player_2.game_status = TIE
        
        self.player_1.endGame(self.board)
        self.player_2.endGame(self.board)