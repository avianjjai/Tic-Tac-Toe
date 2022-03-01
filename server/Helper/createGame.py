from Game import Game
from Data.data import active_games, active_players, lock
import threading

def createGame(p1_id, p2_id):
    lock.acquire()
    game = Game(active_players[p1_id]['player'], active_players[p2_id]['player'])
    active_players[p1_id]['play'] = True
    active_players[p2_id]['play'] = True
    active_games.append(game)
    lock.release()
    
    game.start_Game()

def get2PlayersIdForGame():
    found_id = []
    c = 0
    key = 0
    while key in active_players:
        if c>2:
            break
        if active_players[key]['active']==True and active_players[key]['play']==False:
            found_id.append(key)
            c += 1
        key += 1

    return found_id

def listenGame():
    while True:
        actives = get2PlayersIdForGame()
        if len(actives) == 2:
            p1_id = actives[0]
            p2_id = actives[1]
            game = threading.Thread(target=createGame, args=(p1_id, p2_id))
            game.start()


