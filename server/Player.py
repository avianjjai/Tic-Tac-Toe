from Board import Board
from Constants import WIN, LOSS, TIE, PLAY
import pickle

class Player:
    def __init__(self, addr, pointer, name: str) -> None:
        self.addr = addr
        self.pointer = pointer
        self.name = name
        self.piece = ''
        self.game_status = PLAY
    
    def win_or_not(self, board: Board):
        return board.isWin(self.piece)

    def endGame(self, board: Board):
        send = pickle.dumps({'type': 'END', 'data': board.board, 'result': self.game_status})
        self.pointer.send(send)

        

    def play(self, board: Board):
        send = pickle.dumps({'type': 'PLAY', 'data': board.board})
        print('Send: ' + self.name)
        self.pointer.send(send)

        data = pickle.loads(self.pointer.recv(1024))
        if data['type'] == 'UPDATE':
            board.set(data['data'])

        return self.win_or_not(board)