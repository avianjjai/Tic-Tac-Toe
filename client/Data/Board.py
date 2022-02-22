from UI.Board import Board as UI_Board
import API.api as api
import pickle
import threading

class Board(UI_Board):
    def __init__(self, root, piece, server = None) -> None:
        super().__init__(root, self.click)
        self.server = server
        self.active = False
        self.data = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        self.piece = piece
        self.feed(self.data)

        thr = threading.Thread(target=api.listen, args=(server, self))
        thr.start()


    def update(self, data):
        self.data = data
        self.feed(self.data)

    def __isValid(self, row: int, col: int):
        return row>=0 and row<=2 and col>=0 and col<=2 and self.data[row][col] == ''

    def click(self, row, col):
        if not self.active or not self.__isValid(row, col):
            return
        
        self.data[row][col] = self.piece
        self.feed(self.data)
        self.active = not self.active

        send = pickle.dumps({'type': 'UPDATE', 'data': self.data})
        self.server.send(send)

    def set(self, row: int, col: int, piece: str):
        if not self.__isValid(row, col):
            return False
        
        self.data[row][col] = piece
        return True
