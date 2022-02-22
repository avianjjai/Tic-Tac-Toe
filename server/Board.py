class Board:
    def __init__(self) -> None:
        self.board = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]

    def __winByRow(self, row: int, piece: str):
        for col in range(3):
            if self.board[row][col] != piece:
                return False
        return True

    def __winByCol(self, col: int, piece: str):
        for row in range(3):
            if self.board[row][col] != piece:
                return False
        return True

    def __winByMainDiagonal(self, piece: str):
        for i in range(3):
            if self.board[i][i] != piece:
                return False
        return True

    def __winByAltDiagonal(self, piece: str):
        for i in range(3):
            if self.board[i][2-i] != piece:
                return False
        return True

    def isWin(self, piece: str):
        for row in range(3):
            if self.__winByRow(row, piece):
                return True
        
        for col in range(3):
            if self.__winByCol(col, piece):
                return True

        return self.__winByMainDiagonal(piece) or self.__winByAltDiagonal(piece)

    def endGame(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True

    def set(self, data):
        self.board = data
        return True