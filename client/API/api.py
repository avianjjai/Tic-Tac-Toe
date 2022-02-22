import pickle

def listen(server, board=None):
    while True:
        data = pickle.loads(server.recv(1024))
        print('Your Turn')
        if data['type'] == 'PLAY':
            board.update(data['data'])
            board.active = not board.active

        if data['type'] == 'END':
            board.update(data['data'])
            board.active = False
            print('Game Result:', data['result'])
            break

        if data['type'] == 'HAND SACK':
            pass
    
    # server.close()
    # del board
    