from Board import Board
from Player import Player

class Game:
    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.board = Board()
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = None
        self.__TURN = True

    def __winMessage(self, player: Player):
        print('\n********************** Winner : {} **********************\n'.format(player.name))

    def __tieMessage(self):
        print('\n************************** Tie **************************\n')
        print('Tie !!!')

    def __next_move(self):
        if self.__TURN:
            self.winner = self.player_1 if self.player_1.play(self.board) else None
        else:
            self.winner = self.player_2 if self.player_2.play(self.board) else None
        self.__TURN = not self.__TURN

    def start_Game(self):
        while not self.board.endGame():
            self.__next_move()
            if self.winner:
                break

        if self.winner:
            self.__winMessage(self.winner)
        else:
            self.__tieMessage()