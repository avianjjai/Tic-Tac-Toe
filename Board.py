class Board:
    def __init__(self) -> None:
        self.board = [
            [' ', 'c1', 'c2', 'c3'],
            ['r1', '.', '.', '.'],
            ['r2', '.', '.', '.'],
            ['r3', '.', '.', '.']
        ]

    def display_board(self):
        for row in self.board:
            for col in row:
                print('%-5s'%(col), end='')
            print('')

    def __winByRow(self, row: int, piece: str):
        for col in range(1, 4):
            if self.board[row][col] != piece:
                return False
        return True

    def __winByCol(self, col: int, piece: str):
        for row in range(1, 4):
            if self.board[row][col] != piece:
                return False
        return True

    def __winByMainDiagonal(self, piece: str):
        for i in range(1, 4):
            if self.board[i][i] != piece:
                return False
        return True

    def __winByAltDiagonal(self, piece: str):
        for i in range(1, 4):
            if self.board[i][4-i] != piece:
                return False
        return True

    def isWin(self, piece: str):
        for row in range(1, 4):
            if self.__winByRow(row, piece):
                return True
        
        for col in range(1, 4):
            if self.__winByCol(col, piece):
                return True

        return self.__winByMainDiagonal(piece) or self.__winByAltDiagonal(piece)

    def __isValid(self, row: int, col: int):
        return row>=1 and row<=3 and col>=1 and col<=3 and self.board[row][col] == '.'

    def endGame(self):
        for row in range(1, 4):
            for col in range(1, 4):
                if self.board[row][col] == '.':
                    return False
        return True

    def set(self, row: int, col: int, piece: str):
        if not self.__isValid(row, col):
            return False
        
        self.board[row][col] = piece
        return True