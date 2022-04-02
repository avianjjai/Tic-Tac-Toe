from tkinter import *
import socket
from Constants import WIN, LOSS, TIE, RUNNING
from Data.Board import Board
import pickle

def main():
    server = socket.socket()
    SERVER_PORT = 3000
    # SERVER_IP = '127.0.0.1'
    SERVER_IP = '3.89.100.218'
    server.connect((SERVER_IP, SERVER_PORT))

    piece = ''
    active = None
    recv = pickle.loads(server.recv(1024))
    if recv['type'] == 'HAND SACK':
        piece = recv['piece']
    
    root = Tk()
    root.resizable(width=False, height=False)
    board = Board(root, piece, server)
    root.mainloop()