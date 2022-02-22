import socket
from Constants import WIN, LOSS, TIE, RUNNING

def main():
    s = socket.socket()
    PORT = 3000
    s.connect(('127.0.0.1', PORT))

    name = input(s.recv(1024).decode())
    s.send(name.encode())

    recv = ''
    send = ''
    while True:
        recv, status = s.recv(1024).decode().split('|')
        if status == RUNNING:
            send = input(recv)
            s.send(send.encode())
        else:
            print(recv)
            break
        
    s.close()