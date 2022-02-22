from Board import Board
from Constants import WIN, LOSS, TIE, RUNNING

class Player:
    def __init__(self, addr, pointer, name: str) -> None:
        self.addr = addr
        self.pointer = pointer
        self.name = name
        self.piece = ''
        self.game_status = RUNNING
    
    def disp(self):
        print(self.addr)


    def win_or_not(self, board: Board):
        return board.isWin(self.piece)

    def endGame(self, board: Board):
        send = '\n********************** Final Board **********************\n'
        send += board.display_board()
        if self.game_status == 'WIN':
            send += '\n********************** You Win **********************\n' + '|' + WIN
        elif self.game_status == 'LOSS':
            send += '\n********************** You Lossed **********************\n' + '|' + LOSS
        else:
            send += '\n********************** Game Tie **********************\n' + '|' + TIE
        self.pointer.send(send.encode())

        

    def play(self, board: Board):
        send = ''
        send += '********************** Player : Your Turn **********************'
        send += board.display_board()
        send += 'Enter (row-number col-number): '
        send += '|' + RUNNING
        self.pointer.send(send.encode())

        row, col = list(map(int, self.pointer.recv(1024).decode().strip().split()))
        while not board.set(row, col, self.piece):
            send = 'Wrong Position !!! Try Again\n'
            send += 'Enter (row-number col-number): '
            send += '|' + RUNNING
            self.pointer.send(send.encode())
            row, col = list(map(int, self.pointer.recv(1024).decode().strip().split()))
            

        return self.win_or_not(board)
        # print('********************** Player : {} **********************'.format(self.name))
        # board.display_board()
        # row, col = list(map(int, input('Enter (row-number col-number): ').strip().split()))
        # while not board.set(row, col, self.piece):
        #     print('Wrong Position !!! Try Again !!!')
        #     row, col = list(map(int, input('Enter (row-number col-number): ').strip().split()))
                
        # board.display_board()
        # print()
        # return self.win_or_not(board)