from random import randint
winner = None

class Board:
    def __init__(self):
        self.board = [["?","?","?"],["?","?","?"],["?","?","?"]]
        self.totalSymbols = 0
        self.player_turn = None
    
    def place(self,symbol,column,row):
        self.board[row][column] = symbol

    def print_board(self):
        print("\n {0} | {1} | {2} \n _________ \n {3} | {4} | {5} \n _________ \n {6} | {7} | {8} \n".format(self.board[0][0],self.board[0][1],self.board[0][2],self.board[1][0],self.board[1][1],self.board[1][2],self.board[2][0],self.board[2][1],self.board[2][2]))

class Defense:
    def __init__(self):
        self.row = None
        self.column = None

class Offense:
    def __init__(self):
        self.column = None
        self.row = None

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
        self.game_type = None
        self.current_turn = None
        self.board = Board()
    
    # Game Setup
    def get_game_type(self):
        self.game_type = input("Which game would you like to play? PvP (P) / Beginner (B) / Intermediate (I) / Advanced (A) / Expert (E): ")
        while self.game_type not in ["p","P","b","B","i","I","a","A","e","E"]:
            print("That is an invalid option. Please select again")
            self.game_type = input("Which game would you like to play? PvP (P) / Beginner (B) / Intermediate (I) / Advanced (A) / Expert (E): ")
    
    def get_order(self):
        if self.game_type not in ["p","P"]:
            order = input("Would you like to go first (F) or second (S)?: ")
            while order not in ["f","F","s","S"]:
                print("That is an invalid option. Please select again")
                order = input("Would you like to go first (F) or second (S)?: ")
            return order
    
    def player_setup(self):
        if self.game_type in ["b","B","i","I","a","A","e","E"]:
            order = self.get_order()
            if order == "f" or order == "F":
                self.player1 = Player(1,"Human","X")
                self.player2 = Player(2,"Computer","O")
            else:
                self.player1 = Player(1,"Computer","X")
                self.player2 = Player(2,"Human","O")
            self.current_turn = self.player1
        if self.game_type in ["p","P"]:
            self.player1 = Player(1,"Human","X")
            self.player2 = Player(2,"Human","O")
            self.current_turn = self.player1 

    def select_game(self):
        print("Ready to get started? X will be going first.")

        if self.game_type == "p" or self.game_type == "P":
            self.play_game("P")
        if self.game_type == "b" or self.game_type == "B":
            self.play_game("B")
        if self.game_type == "i" or self.game_type == "I":
            self.play_game("I")
        if self.game_type == "a" or self.game_type == "A":
            self.play_game("A")
        #if game_type == "e" or game_type == "E":
            #expert_ai()
  
    # Game Play Helper Methods
    def getInputs(self):
        row = int(input("What row would you like? (1-3) "))
        while row == 0 or row > 3:
            row = int(input("That row is out of range. Please enter row 1, 2, or 3: "))
        column = int(input("What column would you like? (1-3) "))
        while column == 0 or column > 3:
            column = int(input("That column is out of range. Please enter row 1, 2, or 3: "))
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

    # Checker Methods
    def check_row_for_block(self):
        row_id = 0
        for row in self.board.board:
            if row.count(self.get_human_symbol()) == 2 and row.count("?") > 0:
                defender = Defense()
                defender.row = row_id
                defender.column = row.index("?")
                return defender
            row_id += 1
                    
    def check_diagonal_for_block(self):
        diagonal_list = []
        for i in range(3):
            diagonal_list.append(self.board.board[i][i])
        if diagonal_list.count(self.get_human_symbol()) == 2 and diagonal_list.count("?") > 0:
            defender = Defense()
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
            defender = Defense()
            space_id = diagonal_list.index("?")
            defender.row = 2 - space_id
            defender.column = space_id
            return defender

    def check_column_for_block(self):
        current_column = 0
        current_row = 0
        column_list = []
        while current_column < 3:    
            for row in self.board.board:
                column_list.append(row[current_column])
                if column_list.count(self.get_human_symbol()) == 2 and column_list.count("?") > 0:
                    defender = Defense()
                    defender.column = current_row
                    defender.row = column_list.index("?")
                    return defender
        
            column_list = []
            current_column += 1
            current_row += 1
    
    def check_row_to_win(self):
        row_id = 0
        for row in self.board.board:
            if row.count(self.get_computer_symbol()) == 2 and row.count("?") > 0:
                offense = Offense()
                offense.row = row_id
                offense.column = row.index("?")
                return offense
            row_id += 1

    def check_diagonal_to_win(self):
        diagonal_list = []
        for i in range(3):
            diagonal_list.append(self.board.board[i][i])
        if diagonal_list.count(self.get_computer_symbol()) == 2 and diagonal_list.count("?") > 0:
            offense = Offense()
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
            offense = Offense()
            space_id = diagonal_list.index("?")
            offense.row = 2 - space_id
            offense.column = space_id
            return offense

    def check_column_to_win(self):
        current_column = 0
        current_row = 0
        column_list = []
        while current_column < 3:    
            for row in self.board.board:
                column_list.append(row[current_column])
                if column_list.count(self.get_computer_symbol()) == 2 and column_list.count("?") > 0:
                    offense = Offense()
                    offense.column = column_list.index("?")
                    offense.row = current_row
                    return offense
            column_list = []
            current_column += 1
            current_row += 1

    # Game AIs
    def beginner_ai(self):
        # Generates random moves
        row, column = self.random_slot_generation()
        while self.board.board[row][column] != "?":
            row, column = self.random_slot_generation()
        return row, column 

    def intermediate_ai(self):
        # Defensively blocks opponent completion
        blockers = []
        blockers.append(self.check_row_for_block())
        blockers.append(self.check_diagonal_for_block())
        blockers.append(self.check_other_diagonal_for_block())
        blockers.append(self.check_column_for_block())

        if blockers.count(None) != 4:
            success = False
            for i in range(4):
                if blockers[i] and success == False:
                    success = True
                    return blockers[i].row , blockers[i].column

        else:
            return self.beginner_ai()

    def advanced_ai(self):
        # Actively looks for completions for wins and defensively blocks opponent completions
        offensives = []
        offensives.append(self.check_row_to_win())
        offensives.append(self.check_diagonal_to_win())
        offensives.append(self.check_other_diagonal_to_win())
        offensives.append(self.check_column_to_win())
        
        if offensives.count(None) != 4:
            success = False
            for i in range(4):
                if offensives[i] and success == False:
                    success = True  
                    return  offensives[i].column, offensives[i].row   
        else:
            return self.intermediate_ai() 

    # Game Play        
    def play_game(self, ai):
        row = None
        column = None
        while self.board.totalSymbols < 9:
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

            self.board.place(self.current_turn.symbol,column,row)
            self.board.totalSymbols += 1

            if self.current_turn.order == 1:
                self.current_turn = self.player2
            else:
                self.current_turn = self.player1

            if self.board.totalSymbols >= 5:
                check_1 = checkForWinnerRow(self.board)
                check_2 = checkForWinnerColumn(self.board)
                check_3 = checkForWinnerDiagonal(self.board)
                check_4 = checkForWinnerOtherDiagonal(self.board)

                if check_1 or check_2 or check_3 or check_4:
                    print("The winner is" + winner)
                    self.board.print_board()
                    break
            self.board.print_board()

        if self.board.totalSymbols == 9:
            print("It's a tie!!")

    def execute_game(self):
        new_game.get_game_type()
        new_game.player_setup()
        new_game.select_game()

#def expert_ai():
    # Perfect play, always at least draws

## Game winning checks ##

def checkForWinnerRow(board):
    global winner
    for row in board.board:
        if row.count("X") == 3:
            winner = " X"
            return True 
        elif row.count("O") == 3:
            winner = " O"
            return True

def checkForWinnerColumn(board):
    global winner
    x_total = 0
    o_total = 0
    current_column = 0
    while current_column < 3:    
        for row in board.board:
            if row[current_column] == "X":
                x_total += 1
            if row[current_column] == "O":
                o_total += 1
        if x_total == 3:
            winner = " X"
            return True
        if o_total == 3:
            winner = " O"
            return True
        o_total = 0
        x_total = 0 
        current_column += 1

def checkForWinnerDiagonal(board):
    global winner
    o_total = 0
    x_total = 0
    for i in range(3):
        if board.board[i][i] == "X":
            x_total += 1
        if board.board[i][i] == "O":
            o_total += 1
    if o_total == 3:
        winner = " O"
        return True
    if x_total == 3:
        winner = " X"
        return True

def checkForWinnerOtherDiagonal(board):
    global winner
    o_total = 0
    x_total = 0
    z = 3
    for i in range(3):
        z -= 1
        if board.board[i][z] == "X":
            x_total += 1
        if board.board[i][z] == "O":
            o_total += 1
    if o_total == 3:
        winner = " O"
        return True
    if x_total == 3:
        winner = " X"
        return True

## Beginning of game play ##
print("Welcome to tic-tac-toe!")
new_game = Game()
new_game.execute_game()






