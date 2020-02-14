from tic_tac_toe import Game, Player
from tabulate import tabulate

games_to_play_counter = 1000
games_to_play = games_to_play_counter
all_games = []

ai_1 = "E"
ai_2 = "A"

while games_to_play_counter > 0:
    game = Game()
    game.player1 = Player(1, ai_1, "X")
    game.player2 = Player(2, ai_2, "O")
    game.current_turn = game.player1
    winner = game.ai_vs_ai()
    all_games.append(winner)
    games_to_play_counter -= 1

print(all_games)
wins_player_1 = all_games.count("X")
percent_wins_player_1 = wins_player_1 / games_to_play
wins_player_2 = all_games.count("O")
percent_wins_player_2 = wins_player_2 / games_to_play
ties = all_games.count("tie")
percent_ties = ties / games_to_play
print(tabulate([[ai_1,"1", str(wins_player_1),str(percent_wins_player_1)],[ai_2,"2", str(wins_player_2),str(percent_wins_player_2)],["Tie", None, str(ties),str(percent_ties)]],headers=["AI","Turn order","Games won","%"]))
