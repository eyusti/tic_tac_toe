from random import randint
import math
import copy
import unittest

class Board:
    def __init__(self):
        self.board = [["?","?","?"],["?","?","?"],["?","?","?"]]
        self.player_turn = None
    
    def __repr__(self):
        return "{0}|{1}|{2}.{3}|{4}|{5}.{6}|{7}|{8}".format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2])

    def place(self,symbol,column,row):
        self.board[row][column] = symbol

    def print_board(self):
        print("""
            {0} | {1} | {2} 
            _________ 
            {3} | {4} | {5} 
            _________ 
            {6} | {7} | {8} 
            """.format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2]))
    
    ## Game winning checks ##

    def checkForWinnerRow(self):
        for row in self.board:
            if row.count("X") == 3:
                return "X" 
            elif row.count("O") == 3:
                return "O"

    def checkForWinnerColumn(self):  
        for current_column in range(3):
            if all(row[current_column] == "X" for row in self.board):
                return "X"
            if all(row[current_column] == "O" for row in self.board):
                return "O"

    def checkForWinnerDiagonal(self):
        o_total = 0
        x_total = 0
        for i in range(3):
            if self.board[i][i] == "X":
                x_total += 1
            if self.board[i][i] == "O":
                o_total += 1
        if o_total == 3:
            return "O"
        if x_total == 3:
            return "X"

    def checkForWinnerOtherDiagonal(self):
        o_total = 0
        x_total = 0
        z = 3
        for i in range(3):
            z -= 1
            if self.board[i][z] == "X":
                x_total += 1
            if self.board[i][z] == "O":
                o_total += 1
        if o_total == 3:
            return "O"
        if x_total == 3:
            return "X"

    ## Helper methods ##
    def provide_winner(self):
        winner = self.checkForWinnerRow() or self.checkForWinnerColumn() or self.checkForWinnerDiagonal() or self.checkForWinnerOtherDiagonal()
        total_symbols = 0

        if winner:
            return winner

        for i in range(3):
            total_symbols += self.board[i].count("X")
            total_symbols += self.board[i].count("O")    

        if total_symbols == 9:
            winner = "tie"
            return winner

    def get_all_moves(self, player_symbol):
        list_of_all_moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "?":
                    new_move = copy.deepcopy(self)
                    new_move.place(player_symbol, c , r)
                    list_of_all_moves.append((new_move, r , c))
        return list_of_all_moves

    def is_board_empty(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != "?":
                    return False
        return True

class Place:
    def __init__(self):
        self.row = None
        self.column = None

class Player:
    def __init__(self, order, name, symbol):
        self.symbol = symbol
        self.order = order
        self.is_winner = None
        self.name = name

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.current_turn = None
        self.board = Board()
        self.game_type = None
           
    # Game Setup
    def get_game_type(self):
        while True:
            try:
                self.game_type = input("Which game would you like to play? PvP (P) / Beginner (B) / Intermediate (I) / Advanced (A) / Expert (E): ").upper()
                while self.game_type not in ["P","B","I","A","E"]:
                    print("That is an invalid option. Please select again")
                    self.game_type = input("Which game would you like to play? PvP (P) / Beginner (B) / Intermediate (I) / Advanced (A) / Expert (E): ").upper()
            except ValueError:
                print("That is an invalid option. Please select again")
                continue
            else:
                break        
    
    def get_order(self):
        if self.game_type not in ["P"]:
            while True:
                try:
                    order = input("Would you like to go first (F) or second (S)?: ").upper()
                    while order not in ["F","S"]:
                        print("That is an invalid option. Please select again")
                        order = input("Would you like to go first (F) or second (S)?: ").upper()
                except ValueError:
                    print("That is an invalid option. Please select again")
                    continue
                else:
                    break

            return order
    
    def player_setup(self):
        if self.game_type in ["B","I","A","E"]:
            order = self.get_order()
            if order == "F":
                self.player1 = Player(1,"Human","X")
                self.player2 = Player(2,"Computer","O")
            else:
                self.player1 = Player(1,"Computer","X")
                self.player2 = Player(2,"Human","O")
            self.current_turn = self.player1
        if self.game_type in ["P"]:
            self.player1 = Player(1,"Human","X")
            self.player2 = Player(2,"Human","O")
            self.current_turn = self.player1 
  
    # Game Play Helper Methods
    def getInputs(self):
        while True:
            try:
                row = int(input("What row would you like? (1-3) "))
                while row == 0 or row > 3:
                    row = int(input("That row is out of range. Please enter row 1, 2, or 3: "))
            except ValueError:
                print("That is an invalid input")
                continue
            else:
                break
        
        while True:
            try:
                column = int(input("What column would you like? (1-3) "))
                while column == 0 or column > 3:
                    column = int(input("That column is out of range. Please enter row 1, 2, or 3: "))
            except ValueError:
                print("That is an invalid input")
                continue
            else:
                break

        return row - 1, column - 1 
   
    def random_slot_generation(self):
        x = randint(0,2)
        y = randint(0,2)
        return x , y 

    def get_computer_symbol(self):
        if self.player1.name == "Human":
            return self.player2.symbol
        else:
            return self.player1.symbol

    def get_human_symbol(self):
        if self.player1.name == "Human":
            return self.player1.symbol
        else:
            return self.player2.symbol

    def not_current_turn_symbol(self):
        if self.current_turn.symbol == "X":
            return "O"
        if self.current_turn.symbol == "O":
            return "X"

    # Checker Methods
    def check_row_for_block(self):
        row_id = 0
        for row in self.board.board:
            if row.count(self.get_human_symbol()) == 2 and row.count("?") > 0:
                defender = Place()
                defender.row = row_id
                defender.column = row.index("?")
                return defender
            row_id += 1
                    
    def check_diagonal_for_block(self):
        diagonal_list = []
        for i in range(3):
            diagonal_list.append(self.board.board[i][i])
        if diagonal_list.count(self.get_human_symbol()) == 2 and diagonal_list.count("?") > 0:
            defender = Place()
            space_id = diagonal_list.index("?")
            defender.row = space_id
            defender.column = space_id
            return defender

    def check_other_diagonal_for_block(self):
        diagonal_list = []
        z = 2
        for i in range(3):
            diagonal_list.append(self.board.board[z][i])
            z -= 1
        if diagonal_list.count(self.get_human_symbol()) == 2 and diagonal_list.count("?") > 0:
            defender = Place()
            space_id = diagonal_list.index("?")
            defender.row = 2 - space_id
            defender.column = space_id
            return defender

    def check_column_for_block(self):
        for current_column in range(3):  
            column_list = []
            for row in self.board.board:
                column_list.append(row[current_column])
            if column_list.count(self.get_human_symbol()) == 2 and column_list.count("?") > 0:
                defender = Place()
                defender.column = current_column
                defender.row = column_list.index("?")
                return defender

    def check_row_to_win(self):
        row_id = 0
        for row in self.board.board:
            if row.count(self.get_computer_symbol()) == 2 and row.count("?") > 0:
                offense = Place()
                offense.row = row_id
                offense.column = row.index("?")
                return offense
            row_id += 1

    def check_diagonal_to_win(self):
        diagonal_list = []
        for i in range(3):
            diagonal_list.append(self.board.board[i][i])
        if diagonal_list.count(self.get_computer_symbol()) == 2 and diagonal_list.count("?") > 0:
            offense = Place()
            space_id = diagonal_list.index("?")
            offense.row = space_id
            offense.column = space_id
            return offense

    def check_other_diagonal_to_win(self):
        diagonal_list = []
        z = 2
        for i in range(3):
            diagonal_list.append(self.board.board[z][i])
            z -= 1
        if diagonal_list.count(self.get_computer_symbol()) == 2 and diagonal_list.count("?") > 0:
            offense = Place()
            space_id = diagonal_list.index("?")
            offense.row = 2 - space_id
            offense.column = space_id
            return offense

    def check_column_to_win(self):
        for current_column in range(3):    
            column_list = []
            for row in self.board.board:
                column_list.append(row[current_column])
            if column_list.count(self.get_computer_symbol()) == 2 and column_list.count("?") > 0:
                offense = Place()
                offense.column = current_column
                offense.row = column_list.index("?")
                return offense            

    # Game AIs
    def beginner_ai(self):
        # Generates random moves
        # print(*self.get_all_moves(), sep = "\n")
        row, column = self.random_slot_generation()
        while self.board.board[row][column] != "?":
            row, column = self.random_slot_generation()
        return row, column 

    def intermediate_ai(self):
        # Defensively blocks opponent completion
        blockers = [
            self.check_row_for_block(),
            self.check_diagonal_for_block(),
            self.check_other_diagonal_for_block(),
            self.check_column_for_block()
        ]

        for blocker in blockers:
            if blocker is not None:
                return blocker.row, blocker.column
        return self.beginner_ai()

    def advanced_ai(self):
        # Actively looks for completions for wins and defensively blocks opponent completions
        offensives = [
            self.check_row_to_win(),
            self.check_diagonal_to_win(),
            self.check_other_diagonal_to_win(),
            self.check_column_to_win()
        ]

        for offense in offensives:
            if offense is not None:
                return offense.row, offense.column  

        return self.intermediate_ai() 
    
    def expert_ai(self, board_state, alpha, beta, player):
        # Perfect play, always at least draws
        # Minimax implementation
        # Random first position now obsolete due to alpha beta pruning
        #if board_state.is_board_empty():
            #row, column = self.beginner_ai()
            #return 0 , row, column

        winner = board_state.provide_winner()
        if winner:
            if winner == "tie":
                return 0, None, None
            if winner == self.current_turn.symbol:
                return 1, None, None 
            else:
                return -1, None, None
        
        all_boards = board_state.get_all_moves(player)

        if player == self.current_turn.symbol:
            maxEval = -math.inf 
            best_row = None
            best_column = None
            for board_tuple in all_boards:
                board,t_row,t_column = board_tuple
                eval = self.expert_ai(board,alpha, beta, self.not_current_turn_symbol())
                r_eval, _row, _column = eval
                if r_eval > maxEval:
                    maxEval = r_eval
                    best_row = t_row
                    best_column = t_column
                alpha = max(alpha,r_eval)
                if beta <= alpha:
                    break
    
            return maxEval, best_row, best_column

        else:
            minEval = math.inf
            best_row = None
            best_column = None
            for board_tuple in all_boards:
                board,t_row,t_column = board_tuple
                eval = self.expert_ai(board,alpha, beta, self.current_turn.symbol)
                r_eval, _row, _column = eval
                if r_eval < minEval:
                    minEval = r_eval
                    best_row = t_row
                    best_column = t_column
                beta = min(beta,r_eval)
                if beta <= alpha:
                    break
            return minEval, best_row, best_column

        # Initial Negamax implementation
        """if board_state.is_board_empty():
            row, column = self.beginner_ai()
            return 0 , row, column

        winner = board_state.provide_winner()
        if winner:
            if winner == "tie":
                return 0 , -1 , -1
            if winner == player:
                return 1 , -1 , -1
            else:
                return -1 , -1 , -1

        list_of_possible_moves = board_state.get_all_moves(player)

        if player == "X":
            new_player = "O"
        if player == "O":
            new_player = "X"

        opponent_worst_move, row, column = min((self.expert_ai(move_board, new_player), r, c) for move_board, r , c in list_of_possible_moves)
        score, _row, _column = opponent_worst_move
        return -score , row , column"""

    # Game Play        
    def play_game(self, ai):
        print("Ready to get started? X will be going first.")
        winner = None

        while not winner:
            if self.current_turn.name == "Human":
                row, column = self.getInputs()
                while self.board.board[row][column] != "?":
                    print("That spot is already taken...")
                    row, column = self.getInputs()
            else:
                if ai == "B":
                    row, column = self.beginner_ai()
                elif ai == "I":
                    row, column = self.intermediate_ai()
                elif ai == "A":
                    row, column = self.advanced_ai()
                elif ai == "E":
                    #print(self.board, self.current_turn.symbol, self.get_computer_symbol())
                    _score, row, column = self.expert_ai(self.board,-math.inf,math.inf, self.current_turn.symbol)

            self.board.place(self.current_turn.symbol,column,row)
            self.board.print_board()

            if self.current_turn.order == 1:
                self.current_turn = self.player2
            else:
                self.current_turn = self.player1

            winner = self.board.provide_winner()
            if winner:
                if winner == "X" or winner == "O":
                    print("The winner is " + winner)
                    break
                if winner == "tie":
                    print("It's a " + winner)
                    break

    def ai_vs_ai(self, ai_1, ai_2):
        # This is only used in the tic_tac_toe_player.py script
        winner = None

        if self.current_turn == 1:
            ai= ai_1
        else:
            ai = ai_2

        while not winner:
            if ai == "B":
                row, column = self.beginner_ai()
            elif ai == "I":
                row, column = self.intermediate_ai()
            elif ai == "A":
                row, column = self.advanced_ai()
            elif ai == "E":
                #print(self.board, self.current_turn.symbol, self.get_computer_symbol())
                _score, row, column = self.expert_ai(self.board,-math.inf,math.inf, self.current_turn.symbol)

            self.board.place(self.current_turn.symbol,column,row)
            self.board.print_board()

            if self.current_turn.order == 1:
                self.current_turn = self.player2
            else:
                self.current_turn = self.player1

            winner = self.board.provide_winner()
            if winner:
                if winner == "X" or winner == "O":
                    print("The winner is " + winner)
                    return winner
            
                if winner == "tie":
                    print("It's a " + winner)
                    return winner

    def execute_game(self):
        new_game.get_game_type()
        new_game.player_setup()
        new_game.play_game(self.game_type)

if __name__ == '__main__':
    ## Beginning of game play ##
    print("Welcome to tic-tac-toe!")
    new_game = Game()
    new_game.execute_game()




