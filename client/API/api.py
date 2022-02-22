import pickle

def listen(server, board=None):
    while True:
        data = pickle.loads(server.recv(1024))
        print('Your Turn')
        if data['type'] == 'PLAY':
            board.update(data['data'])
            board.active = not board.active
            board.setTurn(board.active)

        if data['type'] == 'END':
            board.update(data['data'])
            board.active = False
            board.setGameResult(data['result'])
            break

        if data['type'] == 'HAND SACK':
            pass
    
    server.close()
    # del board
    