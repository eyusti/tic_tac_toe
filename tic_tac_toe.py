from random import randint
winner = None
#win_column = None
#win_row = None

class Board:
    def __init__(self):
        self.board = [["?","?","?"],["?","?","?"],["?","?","?"]]
        self.totalSymbols = 0
    
    def symbolSelector(self):
        if self.totalSymbols % 2 == 0:
            return "X"
        else:
            return "O"
    
    def place(self,symbol,column,row):
        self.board[row - 1][column - 1] = symbol

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

def getInputs():
    row = int(input("What row would you like? (1-3) "))
    while row == 0 or row > 3:
        row = int(input("That row is out of range. Please enter row 1, 2, or 3: "))
    column = int(input("What column would you like? (1-3) "))
    while column == 0 or column > 3:
        column = int(input("That column is out of range. Please enter row 1, 2, or 3: "))
    return row, column

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

def random_slot_generation():
    x = randint(0,2)
    y = randint(0,2)
    return x , y

def check_row_for_block(board):
    row_id = 0
    for row in board.board:
        row_id += 1
        if row.count("X") == 2 and row.count("?") > 0:
            defender = Defense()
            defender.row = row_id
            defender.column = row.index("?") + 1
            return defender

def check_diagonal_for_block(board):
    diagonal_list = []
    for i in range(3):
        diagonal_list.append(board.board[i][i])
    if diagonal_list.count("X") == 2 and diagonal_list.count("?") > 0:
        defender = Defense()
        space_id = diagonal_list.index("?")
        defender.row = space_id + 1
        defender.column = space_id + 1
        return defender

def check_other_diagonal_for_block(board):
    diagonal_list = []
    z = 2
    for i in range(3):
        diagonal_list.append(board.board[z][i])
        z -= 1
    if diagonal_list.count("X") == 2 and diagonal_list.count("?") > 0:
        defender = Defense()
        space_id = diagonal_list.index("?")
        defender.row = 3 - space_id
        defender.column = space_id + 1
        return defender

def check_column_for_block(board):
    current_column = 0
    current_row = 0
    column_list = []
    while current_column < 3:    
        for row in board.board:
            column_list.append(row[current_column])
            if column_list.count("X") == 2 and column_list.count("?") > 0:
                defender = Defense()
                defender.column = current_row + 1
                defender.row = column_list.index("?") + 1
                return defender
     
        column_list = []
        current_column += 1
        current_row += 1

def check_row_to_win(board):
    row_id = 0
    for row in board.board:
        row_id += 1
        if row.count("O") == 2 and row.count("?") > 0:
            offense = Offense()
            offense.row = row_id
            offense.column = row.index("?") + 1
            return offense

def check_diagonal_to_win(board):
    diagonal_list = []
    for i in range(3):
        diagonal_list.append(board.board[i][i])
    if diagonal_list.count("O") == 2 and diagonal_list.count("?") > 0:
        offense = Offense()
        space_id = diagonal_list.index("?")
        offense.row = space_id + 1
        offense.column = space_id + 1
        return offense

def check_other_diagonal_to_win(board):
    diagonal_list = []
    z = 2
    for i in range(3):
        diagonal_list.append(board.board[z][i])
        z -= 1
    if diagonal_list.count("O") == 2 and diagonal_list.count("?") > 0:
        offense = Offense()
        space_id = diagonal_list.index("?")
        offense.row = 3 - space_id
        offense.column = space_id + 1
        return offense

def check_column_to_win(board):
    current_column = 0
    current_row = 0
    column_list = []
    while current_column < 3:    
        for row in board.board:
            column_list.append(row[current_column])
            if column_list.count("O") == 2 and column_list.count("?") > 0:
                offense = Offense()
                offense.column = column_list.index("?")
                offense.row = current_row
                return offense
        column_list = []
        current_column += 1
        current_row += 1

def pvp_gameplay():
    game_board = Board()

    while game_board.totalSymbols < 9:
        row, column = getInputs()
        current_symbol = game_board.symbolSelector()

        while game_board.board[row - 1][column - 1] != "?":
            print("That spot is already taken...")
            row, column = getInputs()
            current_symbol = game_board.symbolSelector()


        if game_board.board[row - 1][column - 1] == "?":
            game_board.place(current_symbol,column,row)
            game_board.totalSymbols += 1

        if game_board.totalSymbols >= 5:
            check_1 = checkForWinnerRow(game_board)
            check_2 = checkForWinnerColumn(game_board)
            check_3 = checkForWinnerDiagonal(game_board)
            check_4 = checkForWinnerOtherDiagonal(game_board)
            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                game_board.print_board()
                break
    ###print(board)
        game_board.print_board()
    if game_board.totalSymbols == 9:
        print("It's a tie!!")

def beginner_ai():
    # Generates random moves
    game_board = Board()

    while game_board.totalSymbols < 9:
        if game_board.totalSymbols % 2 == 0:
            row, column = getInputs()
            current_symbol = "X"

            while game_board.board[row - 1][column - 1] != "?":
                print("That spot is already taken...")
                row, column = getInputs()
                current_symbol = "X"

        else:
            row, column = random_slot_generation()
            current_symbol = "O" 
            while game_board.board[row][column] != "?":
                row, column = random_slot_generation()
                current_symbol = "O"                

        if game_board.board[row - 1][column - 1] == "?":
            game_board.place(current_symbol,column,row)
            game_board.totalSymbols += 1

        if game_board.totalSymbols >= 5:
            check_1 = checkForWinnerRow(game_board)
            check_2 = checkForWinnerColumn(game_board)
            check_3 = checkForWinnerDiagonal(game_board)
            check_4 = checkForWinnerOtherDiagonal(game_board)

            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                game_board.print_board()
                break
     ###print(board)
        game_board.print_board()
    if game_board.totalSymbols == 9:
        print("It's a tie!!")

def intermediate_ai():
    # Defensively blocks opponent completion
    game_board = Board()

    while game_board.totalSymbols < 9:
        if game_board.totalSymbols % 2 == 0:
            row, column = getInputs()
            current_symbol = "X"

            while game_board.board[row - 1][column - 1] != "?":
                print("That spot is already taken...")
                row, column = getInputs()
                current_symbol = "X"
        else:
            blockers = []
            blockers.append(check_row_for_block(game_board))
            blockers.append(check_diagonal_for_block(game_board))
            blockers.append(check_other_diagonal_for_block(game_board))
            blockers.append(check_column_for_block(game_board))

            if blockers.count(None) != 4:
                print("test")
                success = False
                for i in range(4):
                    if blockers[i] and success == False:
                        game_board.place("O", blockers[i].column, blockers[i].row)
                        game_board.totalSymbols += 1
                        success = True

            else:
                row, column = random_slot_generation()
                current_symbol = "O" 
                while game_board.board[row][column] != "?":
                    row, column = random_slot_generation()
                    current_symbol = "O"
            
        if game_board.board[row - 1][column - 1] == "?":
            game_board.place(current_symbol,column,row)
            game_board.totalSymbols += 1

        if game_board.totalSymbols >= 5:
            check_1 = checkForWinnerRow(game_board)
            check_2 = checkForWinnerColumn(game_board)
            check_3 = checkForWinnerDiagonal(game_board)
            check_4 = checkForWinnerOtherDiagonal(game_board)

            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                game_board.print_board() 
                break 
     ###print(board)  
        game_board.print_board()
    if game_board.totalSymbols == 9:
        print("It's a tie!!")

def advanced_ai():
    # Actively looks for completions for wins and defensively blocks opponent completions
    game_board = Board()
    while game_board.totalSymbols < 9:
        if game_board.totalSymbols % 2 == 0:
            row, column = getInputs()
            current_symbol = "X"

            while game_board.board[row - 1][column - 1] != "?":
                print("That spot is already taken...")
                row, column = getInputs()
                current_symbol = "X"
        else:
            offensives = []
            offensives.append(check_row_to_win(game_board))
            offensives.append(check_diagonal_to_win(game_board))
            offensives.append(check_other_diagonal_to_win(game_board))
            offensives.append(check_column_to_win(game_board))

            blockers = []
            blockers.append(check_row_for_block(game_board))
            blockers.append(check_diagonal_for_block(game_board))
            blockers.append(check_other_diagonal_for_block(game_board))
            blockers.append(check_column_for_block(game_board))

            if offensives.count(None) != 4:
                success = False
                for i in range(4):
                    if offensives[i] and success == False:
                        game_board.place("O", offensives[i].column, offensives[i].row)
                        success = True
                 
            elif blockers.count(None) != 4:
                success = False
                for i in range(4):
                    if blockers[i] and success == False:
                        game_board.place("O", blockers[i].column, blockers[i].row)
                        game_board.totalSymbols += 1
                        success = True

            else:
                row, column = random_slot_generation()
                current_symbol = "O" 

                while game_board.board[row][column] != "?":
                    row, column = random_slot_generation()
                    current_symbol = "O"
            
        if game_board.board[row - 1][column - 1] == "?":
            game_board.place(current_symbol,column,row)
            game_board.totalSymbols += 1

        if game_board.totalSymbols >= 5:
            check_1 = checkForWinnerRow(game_board)
            check_2 = checkForWinnerColumn(game_board)
            check_3 = checkForWinnerDiagonal(game_board)
            check_4 = checkForWinnerOtherDiagonal(game_board)

            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                game_board.print_board()
                break 
     ###print(board)  
        game_board.print_board()
    if game_board.totalSymbols == 9:
        print("It's a tie!!")

#def expert_ai():
    # Perfect play, always at least draws

print("Welcome to tic-tac-toe!")
game_type = input("Which game would you like to play? PvP (P) / Beginner (B) / Intermediate (I) / Advanced (A) / Expert (E): ")
if game_type == "p" or game_type == "P":
    print("Ready to get started? X will be going first.")
    pvp_gameplay()
if game_type == "b" or game_type == "B":
    print("Ready to get started? X will be going first.")
    beginner_ai()
if game_type == "i" or game_type == "I":
    print("Ready to get started? X will be going first.")
    intermediate_ai()
if game_type == "a" or game_type == "A":
    print("Ready to get started? X will be going first.")
    advanced_ai()
#if game_type == "e" or game_type == "E":
    #print("Ready to get started? X will be going first.")
    #expert_ai()




