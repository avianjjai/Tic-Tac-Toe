import socket
import threading
from Helper.createPlayer import createPlayer

def listenClient():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Server Socket Created Successfully')
    except socket.error as err:
        print('Server Socket creation failed with error %s' %(err))

    PORT = 3000
    server.bind(('', PORT))
    print('socket binded to %s' %(PORT))

    server.listen(5)
    print('socket is listening')

    while True:
        c, addr = server.accept()
        print('Listen:', addr)
        t = threading.Thread(target=createPlayer, args=(c, addr))
        t.start()