from tkinter import *

class Cell:
    def __init__(self, board, height, width, bg, left_x, left_y, row, col, click) -> None:
        self.row = row
        self.col = col
        self.update_cell = click
        self.cell = Canvas(board, bg=bg, height=height, width=width, cursor='target')
        self.val = self.cell.create_text(width/2, height/2, text='', fill='black',  font=('Helvetica 30 bold'))
        self.cell.bind('<Button-1>', lambda e: self.click_cell())
        self.cell.place(x=left_x, y=left_y)

    def feed(self, ch: str):
        self.cell.itemconfig(self.val, text=ch)

    def click_cell(self):
        self.update_cell(self.row, self.col)

class Board:
    def __init__(self, master, click) -> None:
        self.master = master
        master.title('Tic Tac Toe')
        W = int(800*1.0)
        H = int(700*1.0)
        dim = str(W) + 'x' + str(H)
        bg = '#B49D98'
        self.master.geometry(dim)

        self.canvas = Canvas(self.master, bg=bg, height=H, width=W)

        header_h = H*.20
        header_w = W
        self.header = Canvas(self.canvas, bg='#234561', height=header_h, width=header_w)
        self.header.pack()


        game_h = H*.6
        game_w = W
        self.game = Canvas(self.canvas, height=game_h, width=game_w)

        game_col_2_h = game_h
        game_col_2_w = min(game_h, game_w)*.7
        game_col_2_left_x = (game_w - game_col_2_w)/2
        game_col_2_left_y = 0

        game_col_1_h = game_h
        game_col_1_w = (game_w - game_col_2_w)/2
        game_col_1_left_x = 0
        game_col_1_left_y = 0

        game_col_3_h = game_h
        game_col_3_w = game_col_1_w
        game_col_3_left_x = game_col_1_w + game_col_2_w
        game_col_3_left_y = 0

        self.game_col_1 = Canvas(self.game, height=game_col_1_h, width=game_col_1_w)
        self.game_col_1.place(x=game_col_1_left_x, y=game_col_1_left_y)
        self.piece_val = self.game_col_1.create_text(game_col_1_w/2, game_col_1_h/2, text='', fill='black',  font=('Helvetica 25 bold'))

        self.game_col_2 = Canvas(self.game, height=game_col_2_h, width=game_col_2_w)
        self.game_col_2.place(x=game_col_2_left_x, y=game_col_2_left_y)

        board_top_h = (game_col_2_h - game_col_2_w)/2
        board_top_w = game_col_2_w
        self.board_top = Canvas(self.game_col_2, height=board_top_h, width=board_top_w)
        self.turn_status = self.board_top.create_text(board_top_w/2, board_top_h/2, text='', fill='black',  font=('Helvetica 25 bold'))
        self.board_top.pack()


        board_h = game_col_2_w
        board_w = game_col_2_w
        self.board = Canvas(self.game_col_2, height=board_h, width=board_w)

        cell_h = board_h/3
        cell_w = board_w/3

        self.cells = [[None for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.cells[i][j] = Cell(self.board, height=cell_h, width=cell_w, bg='#234561', left_x=cell_w*j, left_y=cell_h*i, row=i, col=j, click=click)

        self.board.pack()

        board_bottom_h = (game_col_2_h - game_col_2_w)/2
        board_bottom_w = game_col_2_w
        self.board_bottom = Canvas(self.game_col_2, height=board_bottom_h, width=board_bottom_w)
        self.game_result = self.board_bottom.create_text(board_bottom_w/2, board_bottom_h/2, text='', fill='Red',  font=('Helvetica 25 bold'))
        self.board_bottom.pack()
        

        self.game_col_3 = Canvas(self.game, height=game_col_3_h, width=game_col_3_w)
        self.game_col_3.place(x=game_col_3_left_x, y=game_col_3_left_y)
        self.game.pack()



        footer_h = H*.20
        footer_w = W
        self.footer = Canvas(self.canvas, bg='#234561', height=footer_h, width=footer_w)
        self.footer.pack()

        self.canvas.pack()

    def setTurn(self, isActive):
        if isActive:
            self.board_top.itemconfig(self.turn_status, text='Your Turn')
        else:
            self.board_top.itemconfig(self.turn_status, text='')

    def setGameResult(self, result: str):
        self.board_bottom.itemconfig(self.game_result, text=result)

    def setPiece(self, piece: str):
        self.game_col_1.itemconfig(self.piece_val, text='Piece: '+piece)

    def feed(self, data):
        for row in range(3):
            for col in range(3):
                self.cells[row][col].feed(data[row][col])

