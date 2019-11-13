from random import randint
board = [["?","?","?"],["?","?","?"],["?","?","?"]]
board_size = 3
winner = None
totalSymbols = 0
blocker_column = None
blocker_row = None

def print_board(board):
    print("\n {0} | {1} | {2} \n _________ \n {3} | {4} | {5} \n _________ \n {6} | {7} | {8} \n".format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2]))

def symbolSelector(symbolNeeded):
    if totalSymbols % 2 == 0:
        return "X"
    else:
        return "O"

def getInputs():
    row = int(input("What row would you like? (1-3) "))
    while row == 0 or row > 3:
        row = int(input("That row is out of range. Please enter row 1, 2, or 3: "))
    column = int(input("What column would you like? (1-3) "))
    while column == 0 or column > 3:
        column = int(input("That column is out of range. Please enter row 1, 2, or 3: "))
    current_symbol = symbolSelector(totalSymbols)
    return row, column, current_symbol

def place(symbol,column,row):
    board[row - 1][column - 1] = symbol

def checkForWinnerRow(board):
    global winner
    for row in board:
        if row.count("X") == board_size:
            winner = " X"
            return True 
        elif row.count("O") == board_size:
            winner = " O"
            return True

def checkForWinnerColumn(board):
    global winner
    x_total = 0
    o_total = 0
    current_column = 0
    while current_column < board_size:    
        for row in board:
            if row[current_column] == "X":
                x_total += 1
            if row[current_column] == "O":
                o_total += 1
        if x_total == board_size:
            winner = " X"
            return True
        if o_total == board_size:
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
        if board[i][i] == "X":
            x_total += 1
        if board[i][i] == "O":
            o_total += 1
    if o_total == board_size:
        winner = " O"
        return True
    if x_total == board_size:
        winner = " X"
        return True

def checkForWinnerOtherDiagonal(board):
    global winner
    o_total = 0
    x_total = 0
    z = board_size
    for i in range(3):
        z -= 1
        if board[i][z] == "X":
            x_total += 1
        if board[i][z] == "O":
            o_total += 1
    if o_total == board_size:
        winner = " O"
        return True
    if x_total == board_size:
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
    for row in board:
        row_id += 1
        if row.count("X") == 2 and row.count("?") > 0:
            blocker_row = row_id
            blocker_column = row.index("?") + 1

def check_diagonal_for_block(board):
    global blocker_column
    global blocker_row
    diagonal_list = []
    for i in range(3):
        diagonal_list.append(board[i][i])
    if diagonal_list.count("X") == 2 and diagonal_list.count("?") > 0:
        space_id = diagonal_list.index("?")
        blocker_row = space_id + 1
        blocker_column = space_id + 1

def pvp_gameplay():
    global totalSymbols
    while totalSymbols <= 9:
        row, column, current_symbol = getInputs()

        while board[row - 1][column - 1] != "?":
            print("That spot is already taken...")
            row, column, current_symbol = getInputs()

        if board[row - 1][column - 1] == "?":
            place(current_symbol,column,row)
            totalSymbols += 1

        if totalSymbols >= 5:
            check_1 = checkForWinnerRow(board)
            check_2 = checkForWinnerColumn(board)
            check_3 = checkForWinnerDiagonal(board)
            check_4 = checkForWinnerOtherDiagonal(board)
            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                break
    ###print(board)
        print_board(board)
    if totalSymbols == 9:
        print("It's a tie!!")

def beginner_ai():
    # Generates random moves
    global totalSymbols
    while totalSymbols <= 9:
        if totalSymbols % 2 == 0:
            row, column, current_symbol = getInputs()
            current_symbol = "X"
            while board[row - 1][column - 1] != "?":
                print("That spot is already taken...")
                row, column, current_symbol = getInputs()
                current_symbol = "X"

        else:
            row, column = random_slot_generation()
            current_symbol = "O" 
            while board[row][column] != "?":
                row, column = random_slot_generation()
                current_symbol = "O"                

        if board[row - 1][column - 1] == "?":
            place(current_symbol,column,row)
            totalSymbols += 1

        if totalSymbols >= 5:
            check_1 = checkForWinnerRow(board)
            check_2 = checkForWinnerColumn(board)
            check_3 = checkForWinnerDiagonal(board)
            check_4 = checkForWinnerOtherDiagonal(board)
            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                break
     ###print(board)
        print_board(board)
    if totalSymbols == 9:
        print("It's a tie!!")

def intermediate_ai():
    # Defensively blocks opponent completion
    global totalSymbols
    global blocker_column
    global blocker_row

    while totalSymbols <= 9:
        if totalSymbols % 2 == 0:
            row, column, current_symbol = getInputs()
            current_symbol = "X"
            while board[row - 1][column - 1] != "?":
                print("That spot is already taken...")
                row, column, current_symbol = getInputs()
                current_symbol = "X"
        else:
            check_row_for_block(board)
            check_diagonal_for_block(board)
            print(blocker_column)
            print(blocker_row)
            if blocker_column is not None:
                place("O", blocker_column, blocker_row)
                totalSymbols += 1
                blocker_column = None
                blocker_row = None
            else:
                row, column = random_slot_generation()
                current_symbol = "O" 
                while board[row][column] != "?":
                    row, column = random_slot_generation()
                    current_symbol = "O"
            
        if board[row - 1][column - 1] == "?":
            place(current_symbol,column,row)
            totalSymbols += 1

        if totalSymbols >= 5:
            check_1 = checkForWinnerRow(board)
            check_2 = checkForWinnerColumn(board)
            check_3 = checkForWinnerDiagonal(board)
            check_4 = checkForWinnerOtherDiagonal(board)
            if check_1 or check_2 or check_3 or check_4:
                print("The winner is" + winner)
                break 
     ###print(board)  
        print_board(board)
    if totalSymbols == 9:
        print("It's a tie!!")

#def advanced_ai():
    # Actively looks for completions for wins and defensively blocks opponent completions

#def expert_ai():
    # Attempts to set up completion attempts as well as preemptivly block completion attempts as well as addressing obvious completions and blocks

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
#if game_type == "a" or game_type == "A":
    #print("Ready to get started? X will be going first.")
    #advanced_ai()
#if game_type == "e" or game_type == "E":
    #print("Ready to get started? X will be going first.")
    #expert_ai()




