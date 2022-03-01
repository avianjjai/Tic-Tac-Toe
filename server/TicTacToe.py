import threading
from Helper.createGame import listenGame
from API.api import listenClient


def main():
    

    threads = []

    listenClient_thread = threading.Thread(target=listenClient, args=())
    listenClient_thread.start()
    threads.append(listenClient_thread)

    listenGame_thread = threading.Thread(target=listenGame, args=())
    listenGame_thread.start()
    threads.append(listenGame_thread)

    # for x in threads:
    #     x.join()

    # server.close()