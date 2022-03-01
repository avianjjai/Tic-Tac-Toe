from ast import Global
from Player import Player
from Data.data import active_players, lock, ID

def createPlayer(c, addr):
    global ID
    player = Player(addr, c, 'random')
    lock.acquire()
    active_players[ID] = {
        'player': player,
        'active': True,
        'play': False
    }
    ID += 1
    lock.release()