from random import randint
#board = [["?","?","?"],["?","?","?"],["?","?","?"]]
#board_size = 3
winner = None
#totalSymbols = 0
blocker_column = None
blocker_row = None
win_column = None
win_row = None

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
    global blocker_column
    global blocker_row
    row_id = 0
    for row in board.board:
        row_id += 1
        if row.count("X") == 2 and row.count("?") > 0:
            blocker_row = row_id
            blocker_column = row.index("?") + 1

def check_diagonal_for_block(board):
    global blocker_column
    global blocker_row
    diagonal_list = []
    for i in range(3):
        diagonal_list.append(board.board[i][i])
    if diagonal_list.count("X") == 2 and diagonal_list.count("?") > 0:
        space_id = diagonal_list.index("?")
        blocker_row = space_id + 1
        blocker_column = space_id + 1

def check_other_diagonal_for_block(board):
    global blocker_column
    global blocker_row
    diagonal_list = []
    z = 2
    for i in range(3):
        diagonal_list.append(board.board[z][i])
        z -= 1
    if diagonal_list.count("X") == 2 and diagonal_list.count("?") > 0:
        space_id = diagonal_list.index("?")
        blocker_row = 3 - space_id
        blocker_column = space_id + 1

def check_column_for_block(board):
    global blocker_column
    global blocker_row
    current_column = 0
    current_row = 0
    column_list = []
    while current_column < 3:    
        for row in board.board:
            column_list.append(row[current_column])
            if column_list.count("X") == 2 and column_list.count("?") > 0:
                blocker_column = current_row + 1
                blocker_row = column_list.index("?") + 1     
        column_list = []
        current_column += 1
        current_row += 1

def check_row_to_win(board):
    global win_column
    global win_row
    row_id = 0
    for row in board.board:
        row_id += 1
        if row.count("O") == 2 and row.count("?") > 0:
            win_row = row_id
            win_column = row.index("?") + 1

def check_diagonal_to_win(board):
    global win_column
    global win_row
    diagonal_list = []
    for i in range(3):
        diagonal_list.append(board.board[i][i])
    if diagonal_list.count("O") == 2 and diagonal_list.count("?") > 0:
        space_id = diagonal_list.index("?")
        win_row = space_id + 1
        win_column = space_id + 1

def check_other_diagonal_to_win(board):
    global win_column
    global win_row
    diagonal_list = []
    z = 2
    for i in range(3):
        diagonal_list.append(board.board[z][i])
        z -= 1
    if diagonal_list.count("O") == 2 and diagonal_list.count("?") > 0:
        space_id = diagonal_list.index("?")
        win_row = 3 - space_id
        win_column = space_id + 1

def check_column_to_win(board):
    global win_column
    global win_row
    current_column = 0
    current_row = 0
    column_list = []
    while current_column < 3:    
        for row in board.board:
            column_list.append(row[current_column])
            if column_list.count("O") == 2 and column_list.count("?") > 0:
                win_column = column_list.index("?")
                win_row = current_row
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
    global blocker_column
    global blocker_row

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
            check_row_for_block(game_board)
            check_diagonal_for_block(game_board)
            check_other_diagonal_for_block(game_board)
            check_column_for_block(game_board)
            if blocker_column is not None:
                game_board.place("O", blocker_column, blocker_row)
                game_board.totalSymbols += 1
                blocker_column = None
                blocker_row = None
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
    global blocker_column
    global blocker_row
    global win_column
    global win_row
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
            check_row_to_win(game_board)
            check_diagonal_to_win(game_board)
            check_other_diagonal_to_win(game_board)
            check_column_to_win(game_board)
            check_row_for_block(game_board)
            check_diagonal_for_block(game_board)
            check_other_diagonal_for_block(game_board)
            check_column_for_block(game_board)
            print(win_column)
            print(win_row)
            print(blocker_column)
            print(blocker_row)
            if win_column is not None:
                game_board.place("O", win_column, win_row) 
            elif blocker_column is not None:
                game_board.place("O", blocker_column, blocker_row)
                game_board.totalSymbols += 1
                blocker_column = None
                blocker_row = None
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




