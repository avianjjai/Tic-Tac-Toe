from tkinter import *
import socket
from Constants import WIN, LOSS, TIE, RUNNING
from Data.Board import Board
import pickle

# def main():
#     s = socket.socket()
#     PORT = 3000
#     s.connect(('127.0.0.1', PORT))

#     name = input(s.recv(1024).decode())
#     s.send(name.encode())

#     recv = ''
#     send = ''
#     while True:
#         recv, status = s.recv(1024).decode().split('|')
#         if status == RUNNING:
#             send = input(recv)
#             s.send(send.encode())
#         else:
#             print(recv)
#             break
        
#     s.close()

def main():
    server = socket.socket()
    SERVER_PORT = 3000
    SERVER_IP = '127.0.0.1'
    server.connect((SERVER_IP, SERVER_PORT))

    # recv = ''
    # send = ''
    # while True:
    #     recv, status = server.recv(1024).decode().split('|')
    #     if status == RUNNING:
    #         send = input(recv)
    #         server.send(send.encode())
    #     else:
    #         print(recv)
    #         break
        
    # server.close()

    piece = ''
    active = None
    recv = pickle.loads(server.recv(1024))
    if recv['type'] == 'HAND SACK':
        piece = recv['piece']
    
    root = Tk()
    root.resizable(width=False, height=False)
    board = Board(root, piece, server)
    root.mainloop()