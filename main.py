from Game import Game
from Player import Player
        
def main():
    p1_name = input('Name(Player 1): ')
    p1_piece = input('Piece(Player 1): ')

    print()

    p2_name = input('Name(Player 2): ')
    p2_piece = input('Piece(Player 2): ')
    
    player_1 = Player(p1_name, p1_piece)
    player_2 = Player(p2_name, p2_piece)

    game = Game(player_1, player_2)
    game.start_Game()

if __name__ == '__main__':
    main()