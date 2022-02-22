import socket
import threading
from Game import Game
from Player import Player

lock = threading.Lock()
active_users = []
def createPlayer(c, addr):
    player = Player(addr, c, 'random')
    lock.acquire()
    active_users.append(player)
    lock.release()


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Server Socket Created Successfully')
    except socket.error as err:
        print('Server Socket creation failed with error %s' %(err))

    PORT = 3000
    s.bind(('', PORT))
    print('socket binded to %s' %(PORT))

    s.listen(5)
    print('socket is listening')

    count = 0
    while count < 2:
        c, addr = s.accept()
        t = threading.Thread(target=createPlayer, args=(c, addr))
        t.start()

        count += 1

    while len(active_users) < 2:
        pass

    game = Game(active_users[0], active_users[1])
    game.start_Game()
    s.close()