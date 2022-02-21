from Board import Board

class Player:
    def __init__(self, name: str, piece: str) -> None:
        self.name = name
        self.piece = piece

    def win_or_not(self, board: Board):
        return board.isWin(self.piece)

    def play(self, board: Board):
        print('********************** Player : {} **********************'.format(self.name))
        board.display_board()
        row, col = list(map(int, input('Enter (row-number col-number): ').strip().split()))
        while not board.set(row, col, self.piece):
            print('Wrong Position !!! Try Again !!!')
            row, col = list(map(int, input('Enter (row-number col-number): ').strip().split()))
            
        board.display_board()
        print()
        return self.win_or_not(board)