from colorama import Fore, Style
import turtle

#Makes turtle screen object, an actual turtle object, and makes the screen reset everytime the code starts to reset the turtle screen
screen = turtle.Screen()
screen.reset()    
t = turtle.Turtle()
def make_R():
    """Function that has no parameters and makes the letter R with the turtle"""
    t.penup()
    t.goto(-200,120)
    t.pendown()
    t.goto(-200,200)
    t.goto(-150,200)
    t.goto(-150,175)
    t.goto(-200,175)
    t.goto(-150,120)
    t.penup()
def make_E(x):
    """Function that has a parameter of (x) which will change the position of the E made in turtle as Red and Yellow both have an E"""
    t.goto(-125-x,200)
    t.pendown()
    for a in range(200,120,-40):
        t.goto(-75-x,a)
        t.goto(-125-x,a)
        t.goto(-125-x,a-40)
    t.goto(-75-x,120)
    t.penup()
def make_D():
    """Function that has no parameters and makes the letter D with the turtle"""
    t.goto(-50,200)
    t.pendown()
    t.goto(-50,120)
    t.circle(40,180)
    t.penup()
def make_W(x,y):
    """Function that takes two parameters (x,y) that will change the x and y coordinates of a turtle W accordingly if red or yellow wins"""
    t.goto(-200+x,100+y)
    t.pendown()
    t.goto(-200+x,20+y)
    t.goto(-175+x,75+y)
    t.goto(-150+x,20+y)
    t.goto(-150+x,100+y)
    t.penup()
def make_I():
    """Function that has no parameters and makes the I in win with turtle"""
    t.goto(-125,100)
    t.pendown()
    t.goto(-75,100)
    t.goto(-100,100)
    t.goto(-100,20)
    t.goto(-125,20)
    t.goto(-75,20)
    t.penup()
def make_N():
    """Function that has no parameters and makes the N in win with the turtle"""
    t.goto(-50,20)
    t.pendown()
    t.goto(-50,100)
    t.goto(-10,20)
    t.goto(-10,100)
    t.penup()
def make_S(angle):
    """Function that has one parameter (angle) which will change which way the turtle is facing such that the S for red and yellow
       will be made properly"""
    t.right(angle)
    t.goto(35,20)
    t.pendown()
    t.backward(20)
    t.forward(20)
    t.circle(20,180)
    t.penup()
    t.goto(35,100)
    t.pendown()
    t.backward(20)
    t.forward(20)
    t.circle(20,180)
def make_Y():
    """Function that has no parameters and makes a Y with a turtle object"""
    t.penup()
    t.goto(-250,200)
    t.pendown()
    t.goto(-225,175)
    t.goto(-200,200)
    t.goto(-225,175)
    t.goto(-225,120)
    t.penup()
def make_L(x):
    """Function that has parameter (x) which will be used to change the x-coordinates of where the L is made as Yellow has two L's"""
    t.goto(-100+x,200)
    t.pendown()
    t.goto(-100+x,120)
    t.goto(-50+x,120)
    t.penup()
def make_O():
    """Function with no parameters and makes an O for the word yellow"""
    t.goto(75,120)
    t.pendown()
    t.circle(43)
    t.penup()
def yellow_wins():
    """Function that has no parameter and will call previous functions to say 'Yellow Wins'"""
    #Will make the text yellow
    t.pencolor("yellow")
    #Makes the turtle go really fast such that it's almost instant
    t.speed(999)
    #Hides the turtle such that only the text can be seen
    t.hideturtle()
    #Makes the letters more thicker
    t.pensize(5)
    make_Y()
    make_E(50)
    make_L(0)
    make_L(75)
    make_O()
    make_W(335,100)
    make_W(0,0)
    make_I()
    make_N()
    make_S(0)
def red_wins():
    """Function that has no parameter and will call previous functions to say 'Red Wins'"""
    t.pencolor("red")
    t.speed(999)
    t.hideturtle()
    t.pensize(5)
    make_R()
    make_E(0)
    make_D()
    make_W(0,0)
    make_I()
    make_N()
    make_S(180)
def valid_color():
    """This function takes no input and will return a valid color until the user finally enters a valid color name"""
    #Loops till a valid color name of 'red' or 'yellow' is inputted
    while True:
        try:
            color_turn = input('\nThat is an invalid input, please input either Red or Yellow: ')
            if color_turn.lower() != 'red': 
                if color_turn.lower() != 'yellow':
                    raise ValueError
            break
        except:
            continue
    return color_turn
def first_player():
    """Simply prints which player will go first with the only input being which color player 1 chose"""
    try:
        #Calls for which color player 1 will be, if it's yellow, then player 1 will go first and if red, then player 2 will go first 
        print('Please input which color player 1 will be (',Fore.RED + Style.BRIGHT + '\bRed', Style.RESET_ALL + 'or', Fore.YELLOW + Style.BRIGHT + 'Yellow', Style.RESET_ALL +'\b): ')
        color_turn = input().lower()
        #Raises error if it's an invalid color or word
        if color_turn != 'red':
               if color_turn != 'yellow':
                   raise ValueError
    except:
        #Loops till the color inputted is fully valid
        color_turn = valid_color().lower()
    if color_turn == 'red':
        print('\nPlayer 2 is', Style.BRIGHT + Fore.YELLOW + 'Yellow', Style.RESET_ALL + 'and Player 1 is', Style.BRIGHT + Fore.RED + 'Red', Style.RESET_ALL + '\b, Player 2 will go first.\n')
        return 2
    else:
        print('\nPlayer 1 is', Style.BRIGHT + Fore.YELLOW + 'Yellow', Style.RESET_ALL + 'and Player 2 is', Style.BRIGHT + Fore.RED + 'Red', Style.RESET_ALL + '\b, Player 1 will go first.\n')
        return 1
#Prints the instructions on how to use the program to play Connect 4       
def print_instructions():
    """This code simply prints the instructions of Connect 4"""
    """Also utlizes the colorama package which will use the Fore and Style function.
       The Fore function will change the actual color and the style function will be used to make the text brighter and to also reset the colors as needed"""
    print(Fore.CYAN +'*****', Style.BRIGHT +'Welcome to', Fore.RED, Style.BRIGHT + '\bConnect', Fore.YELLOW + '4', Style.RESET_ALL +'\b!', Fore.CYAN + '\b*****\n')
    print(Fore.RED, Style.BRIGHT + '\bConnect',  Fore.YELLOW + '4', Fore.BLUE + 'works by having two players with 2 different colored coins,', Fore.RED + 'Red', Fore.BLUE + 'and',  Fore.YELLOW + '\b Yellow', Fore.BLUE + '\b.\n')
    print(Fore.BLUE + "\bEach player's goal is to", Fore.GREEN + "align", Fore.BLUE + "their coins on the game board", Fore.GREEN + "(7 columns and 6 rows)", Fore.BLUE + "such that their coin has", Fore.YELLOW + '4', Fore.MAGENTA + 'in-a-row', Fore.GREEN + 'either vertically, horizontally, or diagonally.\n')
    print(Fore.BLUE + 'But there can not be any color blocking your', Fore.YELLOW + '4', Fore.MAGENTA + 'in-a-row', Fore.BLUE + '\b, and in the event that no player gets', Fore.YELLOW + '4', Fore.MAGENTA + 'in-a-row', Fore.BLUE + '\b, the game will end in a', Fore.RED + 'tie.\n')
    print('Players also must', Fore.GREEN + 'choose', Fore.BLUE + 'which column they wish to', Fore.GREEN + 'play in', Fore.BLUE + 'and their coin will', Fore.GREEN + 'drop', Fore.BLUE + 'into that column.\n')
    print('If a coin has already been placed into that row, then the coin will be put', Fore.GREEN + 'on top of', Fore.BLUE + 'the coin (', Fore.RED +'\bcannot', Fore.BLUE + 'have more than', Fore.GREEN + '7', Fore.BLUE + 'coins per column).\n')
    print(Fore.CYAN + '\n***** How to Use the Program *****\n')
    print(Fore.BLUE + "You'll first be asked which color you want to go first,", Fore.YELLOW + "yellow", Fore.BLUE + "will go first with", Fore.RED + "red", Fore.BLUE + "after.\n")
    print("Each turn will be", Fore.GREEN + "swapped", Fore.BLUE +"after each play", Fore.GREEN + "per turn", Fore.BLUE + "has been made.\n")
    print("You'll be shown the gameboard which will show the available spaces and will be asked which colummn number", Fore.GREEN + "(1-7)", Fore.BLUE + "you wish to", Fore.GREEN + "place", Fore.BLUE+ "your coin in.\n")
    print("When either player has gotten", Fore.YELLOW + '4', Fore.MAGENTA + 'in-a-row', Fore.BLUE + "\b, the program will print the", Fore.WHITE + "winner", Fore.BLUE + "and the game will be", Fore.RED + "over.\n", Fore.CYAN + '\bIf you want to end the game early, input "q" at any turn.')
    print(Fore.CYAN + "\nSo let's begin!", Style.RESET_ALL)
    
print_instructions()
#Used for turtle logic checking for printing the winner and for also making the color of each player's tile
original_first_player = first_player()

def print_board(board, original_first_player):
    """This function prints the entire board row by row evenly
       
       Paramters: Only parameter is the board variable or the list-of-lists to hold the entire board"""
    #Will hold the board as a string
    board_as_string = '\b'
    #Loop starts with the row and inner for loop will go by column
    for row in board:
        #Goes column by column per row
        for column in row:
            if column == '.':
                #Makes it a standard white-colored dot
                board_as_string += Style.RESET_ALL + column + ' '
            elif column == str(original_first_player):
                #If the index being analyzed is the same as the original color, then it will always be yellow, if not then it's red
                board_as_string += Style.BRIGHT + Fore.YELLOW + column + ' '
                Style.RESET_ALL
            else:
                board_as_string += Style.BRIGHT + Fore.RED + column + ' '
                Style.RESET_ALL
        board_as_string += Style.RESET_ALL + '\n'
    return board_as_string
def print_turtle_winner(player):
    """This function takes only the winning player as the input and will print out which color has won with turtle graphics"""
    if original_first_player == int(player):
        yellow_wins()
        screen.update()
    else:
        red_wins()
        screen.update()
def check_vertical(board, player):
    """This function checks to see if there are any vertical coins of the same color that are 4 in a row
       In the event that there is 4 in a row, the function will return true and reassign game_over to be true
       such that the game will end.
       
       Parameters: (board) which will always be the board variable which represents the game board as a list of lists
       """
    #Will hold however many color tiles/coins are in a row and will return true when there's 4 of a certain color in a row
    in_a_row = 0
    #Will go column by column first then the row for player 1
    for column in range(7):
       for row in range(6):
           #For when there's a coin for player 1 present
           if board[row][column] == player:
               in_a_row += 1
               if in_a_row == 4:
                   print('Here is the board:\n', print_board(board, original_first_player))
                   print(f'The winner is Player {player}\n')
                   print_turtle_winner(player)
                   return True
           #Causes the loop to break when player 2's coin is placed instead of player 1
           #For when there's an empty space
           else:
               in_a_row = 0
       in_a_row = 0
def check_horizontal(board, player):
    """This function checks to see if there are any Horizontal coins of the same color that are 4 in a row
       In the event that there is 4 in a row, the function will return true and reassign game_over to be true
       such that the game will end.
       
       Parameters: (board) which always be the board variable which represents the game board as a list of lists
       """
    #Will hold however many color tiles/coins are in a row and will return true when there's 4 of a certain color in a row
    in_a_row = 0
    #Will go row by row first then the column for player 1
    for row in range(6):
       for column in range(7):
           #For when there's a coin for player 1 present
           if board[row][column] == player:
               in_a_row += 1
               if in_a_row == 4:
                   print('Here is the board:\n', print_board(board, original_first_player))
                   print(f'The winner is Player {player}\n')
                   print_turtle_winner(player)
                   return True
           #Causes the loop to break when player 2's coin is placed instead of player 1
           else:
               in_a_row = 0
       in_a_row = 0
#Function that will be utilized by the check_diagonal function to see if there are any 4-in-a-row for the specified player
def check_diagonal_right(board, player):
    """"This function will check to see if there are in 4-in-a-row diagonally right for the specified player
        In the event that there is 4 in a row, the function will return true and reassign game_over to be true
        such that the game will end.
    
        Parameters: (board, player) 
        (board) which always be the board variable which represents the game board as a list of lists, 
        and (player) will be the current player be analyzed as a string, so either '1' or '2'"""
    #Will hold however many color tiles/coins are in a row and will return true when there's 4 of a certain color in a row
    in_a_row = 0
    #This will check to see if there are any right diagonals in a row for either player, and will go row by row then column by column
    #Row that is currently being analyzed
    for row in range(6):
        #Starting column for respective row that is being analyzed
        #Maybe lower the range as the column can only go so far???
        for column in range(7):
            if board[row][column] == player:
                in_a_row += 1
                try:
                    #Will hold the next columns to be analyzed
                    next_column = column + 1
                    #Will hold the next row
                    next_row = row +1
                    #Checks the diaganally right index of the board 
                    while next_row < 6:
                        if board[next_row][next_column] == player:
                            in_a_row += 1
                            #For when there's a winner
                            if in_a_row == 4:
                                print('Here is the board:\n', print_board(board, original_first_player))
                                print(f'The winner is Player {player}\n')
                                print_turtle_winner(player)
                                return True
                            next_column += 1
                            next_row += 1
                        else:
                            in_a_row = 0
                            break
                except:
                    in_a_row = 0
                    continue
            else:
                in_a_row = 0
            in_a_row = 0
        in_a_row = 0
    #When no rightward diagonals are found
    return False 
def check_diagonal_left(board, player):
    """"This function will check to see if there are in 4-in-a-row diagonally left for the specified player
        In the event that there is 4 in a row, the function will return true and reassign game_over to be true
        such that the game will end.
    
        Parameters: (board, player) 
        (board) which always be the board variable which represents the game board as a list of lists, 
        and (player) will be the current player be analyzed as a string, so either '1' or '2'"""
    #Holds however many coins or tiles are in-a-row for a player
    in_a_row = 0            
    #Variable that will be to analyze the board the same way as the previous block of code, but backward with while loops
    column = 6
    #This will check to see if there are any left diagonals in a row for either player, and will go row by row then column by column
    for row in range(6):
        while column >= 0:
            if board[row][column] == player:
                in_a_row += 1
                try:
                    #Will hold the next column to be analyzed
                    next_column = column - 1
                    #Will hold the next row
                    next_row = row + 1
                    #Checks diagonally left index of the board
                    while next_row < 6:
                        if board[next_row][next_column] == player:
                            in_a_row += 1
                            #For when there's a winner
                            if in_a_row == 4:
                                print('Here is the board:\n', print_board(board, original_first_player))
                                print(f'The winner is Player {player}\n')
                                print_turtle_winner(player)
                                return True
                            next_column -= 1
                            next_row += 1
                        else:
                            in_a_row = 0
                            break
                except:
                    in_a_row = 0
                    break
            else:
                in_a_row = 0
            in_a_row = 0
            column -= 1
        in_a_row = 0
        column = 6
    #When no rightward diagonals are found
    return False
def valid_input(player):
    """Checks to see if the user inputted a valid column in the range 1-7
       Parameters: (player), only input is the player number as string for formatting"""
    try:
        column = input(f"\nIt is player {player}'s turn, enter which column to place your coin in: ")
        #Will quit the game if the user wants to at this point in time
        if column.lower() == 'q':
            return 'q'
        column = int(column)
        if column < 1 or column > 7:
            raise ValueError
        return column
    except:
        while True:
            try:
                column = int(column)
                while True:
                    if column < 1 or column > 7:
                        column = input('Please input an integer from 1-7: ')
                        #Will quit the game if the user wants to at this point in time
                        if column.lower() == 'q':
                            return 'q'
                        column = int(column)
                    else:
                        return column
            except:
                column = input('Please input an integer from 1-7: ')
                if column.lower() == 'q':
                    return 'q'
                continue
def valid_column(board, column, player):
    """Checks to see if the inputted column number as the parameter is not filled on the game board
       If it is, then the function will return false and the current player will need to choose a different column
       If it is valid, then a tile will be placed in the appropriate column and proper row
       Lists changed in functions are changed outside of them too, so this function will successfully change the board
       
       Parameters are the board itself and then the column number as an integer, and then the player number
       for utilizing the valid_input function for the respective player"""
    #Goes row by row for the specific column, starts at the bottom of the board and goes up for the analysis
    row = 5
    while True:
        while row >= 0:
            if board[row][column] == '.':
                return row, column
            row -= 1
        #Prints when only 1's and 2's are found
        print('That column is filled up! Select a different column please!')
        column = valid_input(player)
        #Will quit the game if the user wants to at this point in time
        if column == 'q':
            return -1,'q'
        column -= 1
        row = 5
def place_piece(board, row, column, player):
    """Will place the actual piece onto the gameboard for the assigned player
       
       Parameters are the game board itself, then the row in which the valid piece will be placed in, then the column
        the valid piece will be placed in and then the player number to determine what type of coin will be placed in that index"""
    if player == 1:
        board[row][column] = '1'
    else:
        board[row][column] = '2'
def reset_board():
    """""Takes no input for the parameter and merely resets the gameboard in the original format as seen in the game function"""
    return     [['.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.'],['.', '.', '.', '.', '.', '.', '.']]
def rematch():
    """Function that has no parameters and will ask for the user if they want to have a rematch, if yes, then the while loop that
       runs the game will repeat, if not, then the program will end"""
    rematch = input('Want a rematch? Enter "C" to continue and enter anything else to exit ')
    if rematch.lower() == 'c':
        #All declared as global variables such that they can be changed accordingly and to save lines of code
        global board
        global turn
        global player
        global original_first_player
        board = reset_board()
        turn = 0
        original_first_player = first_player()
        player = original_first_player
        move_catalog.write('***** GAME END *****\n')
        screen.reset()
        return True
    return False
#Determines which color's turn it is based on user input, will loop till given a valid input
#Prints which player will go first and will hold the starting player as a number
player = original_first_player
#Holds how many turns have passed and will stop when the game board is filled entirely
turn = 0
#List that will hold the entire gameboard
board = [['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.']]
#Opens a file that will keep track of all of the plays made by the players
move_catalog = open('move_list.txt', 'w')
#Will be used to determine if the user wants to have a rematch or not, if True then rematch, if False then the program shall end
con = False
while True:
   print('Here is the board:\n', print_board(board, original_first_player))
   #Will be used to ensure that all code will quit the game no matter where the user says that they want to end (besides choosing the color)
   break_code = False
   #Tells which color's turn it is and asks for the column they want to put their coin in
   if player == 1:
       column = valid_input('1')
       #Will quit the game if the user wants to at this point in time
       if column == 'q':
           if rematch():
               continue
           break
       column = column - 1
       #Tries to see if the column isn't filled and will tell the user if it is and to pick a different column instead
       #Will loop until a valid column is given
       while True:
           #Holds the valid row as an integer and if the column is valid or not
           row, column = valid_column(board, column, '1')
           #Will quit the game if the user wants to at this point in time
           if column == 'q':
               if rematch():
                   con = True
               else:
                   break_code = True
               break
           #Will place the piece on the board, write down the move in the catalog file, and swap which player it is till the game ends
           place_piece(board, row, column, 1)
           move_catalog.write('Move ' + str(turn + 1) + ': Player 1 placed their coin at row ' + str(row) + ' with column ' + str(column) +'\n')
           player = 2
           break
       #For when the user declares a rematch
       if con:
           continue
       #To ensure that the program fully quits as calling quits after trying to place a piece in a filled section would ask the user if they wanted
       #to quit 2 times, this ensures that when they are asked once, that they game will actually end
       if break_code:
           break
   else:
      column = valid_input('2')
      #Will quit the game if the user wants to at this point in time
      if column == 'q':
          if rematch():
              continue
          break
      column = column - 1
      #Tries to see if the column isn't filled and will tell the user if it is and to pick a different column instead
      #Will loop until a valid column is given
      while True:
          #Holds the valid row as an integer and if the column is valid or not
          row, column = valid_column(board, column, '2')
          #Will quit the game if the user wants to at this point in time
          if column == 'q':
              if rematch():
                  con = True
              else:
                  break_code = True
              break
          place_piece(board, row, column, 2)
          move_catalog.write('Move ' + str(turn + 1) + ': Player 2 placed their coin at row ' + str(row) + ' with column ' + str(column) +'\n')
          player = 1
          break
      #Same two statements in previous block of code for Player 1
      if con:
          continue
      if break_code:
          break
   #Checks to see if there are any vertical 4-in-a-rows on the board
   if check_vertical(board, '1') or check_vertical(board, '2'):
        if rematch():
            continue
        move_catalog.write('***** GAME END *****\n')
        break
   #Checks to see if there are any horizontal 4-in-a-rows on the board
   if check_horizontal(board,'1') or check_horizontal(board,'2'):
        if rematch():
            continue
        move_catalog.write('***** GAME END *****\n')
        break
   #Checks to see if there are any diagonal 4-in-a-rows on the board
   if check_diagonal_right(board,'1') or check_diagonal_left(board,'1') or check_diagonal_right(board, '2') or check_diagonal_left(board, '2'):
        if rematch():
            continue
        move_catalog.write('***** GAME END *****\n')
        break
   turn += 1
   #For when a tie has occurred
   if turn == 42:
       print('Here is the board:\n', print_board(board, original_first_player), "\nIt's a tie, there is no winner!\n")
       if rematch():
           continue
       move_catalog.write('***** GAME END *****\n')
       break
move_catalog.close()