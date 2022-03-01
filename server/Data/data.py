import threading

active_players = {}
active_games = []
lock = threading.Lock()
ID = 0