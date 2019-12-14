from tic_tac_toe import Board, Game

def test_expert_ai_blocks_obvious_threat():
    board = Board()
    game = Game()
    board.board = [["?", "?", "?"],["?", "O", "X"], [ "X", "?", "O"]]
    score, row, column = game.expert_ai(board, "X")
    assert(row == 0)
    assert(column == 0)
    assert(score == 0)
