import pytest
import copy
import math
from tic_tac_toe import Board, Game, Player

def test_minimax():
    new_game = Game()
    new_board = Board()
    new_board.board = [["O","O","X"],["X","?","O"],["?","?","X"]]
    new_game.board = new_board
    new_game.player1 = Player(1,"Human", "O")
    new_game.player2 = Player(2,"Computer", "X")
    assert new_game.expert_ai(new_game.board,-math.inf,math.inf,"X") == (1,2,1)

def test_minimax_2():
    new_game = Game()
    new_board = Board()
    new_board.board = [
        ["?","O","?"],
        ["X","O","?"],
        ["O","X","X"]]
    new_game.board = copy.deepcopy(new_board)
    new_game.player1 = Player(1,"Human", "O")
    new_game.player2 = Player(2,"Computer", "X")
    assert new_game.expert_ai(new_game.board,-math.inf,math.inf,"X") == (0,0,2)

def next_move_and_result(player, board_string):
    new_board = Board()
    flat_board = board_string.split()
    board_array = [flat_board[0:3],flat_board[3:6], flat_board[6:9]]
    new_board.board = board_array
    new_game = Game()
    new_game.board = new_board
    new_game.player1 = Player(1,"Human", "O")
    new_game.player2 = Player(2,"Computer", "X")
    result, best_row, best_column = new_game.expert_ai(new_game.board,player)
    board_array[best_row][best_column] = "*"
    new_board_string = "\n    ".join(" ".join(row) for row in board_array)
    return """
    Position score: {}
    {}
    """.format(result, new_board_string)

def test_visual_one():
    assert next_move_and_result("X", """
    O X O
    ? X ?
    ? ? X
    """) == """
    Position score: 1
    O X O
    ? X ?
    ? * X
    """

def test_visual_2():
    assert next_move_and_result("X", """
    O ? ?
    X O ?
    O X X
    """) == """
    Position score: 0
    O ? *
    X O ?
    O X X
    """

def test_visual_3():
    assert next_move_and_result("O", """
    O ? ?
    X O X
    O X X
    """) == """
    Position score: -1
    O ? *
    X O X
    O X X
    """

def test_visual_4():
    assert next_move_and_result("X", """
    X X ?
    O O ?
    ? ? ?
    """) == """
    Position score: 1
    X X *
    O O ?
    ? ? ?
    """

def test_visual_5():
    assert next_move_and_result("X", """
    O X X
    O O ?
    ? ? ?
    """) == """
    Position score: -1
    O X X
    O O ?
    ? ? *
    """