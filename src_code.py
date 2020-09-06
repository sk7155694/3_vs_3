# 3 vs 3 game



def display_table(table):
    print("===============================================")
    print("|| "+table[1]+" ||            || "+table[2]+" ||              || " +table[3]+" ||")
    print("||===||============||===||==============||===||")
    print("||   ||            ||   ||              ||   ||")
    print("||   ||            ||   ||              ||   ||")
    print("||   ||            ||   ||              ||   ||")
    print("||===||============||===||==============||===||")
    print("|| "+table[4]+" ||            || "+table[5]+" ||              || " +table[6]+" ||")
    print("||===||============||===||==============||===||")
    print("||   ||            ||   ||              ||   ||")
    print("||   ||            ||   ||              ||   ||")
    print("||   ||            ||   ||              ||   ||")
    print("||===||============||===||==============||===||")
    print("|| "+table[7]+" ||            || "+table[8]+" ||              || " +table[9]+" ||")
    print("===============================================")
    
# function for choosing the players marker
from IPython.display import clear_output
def player_marker():
    
    marker=0
    while not (marker == "#" or marker == "@"):
        
        marker = input("enter the choice [#] or [@]")
        if not (marker == "#" or marker == "@") :
                clear_output()
                print("you are entering wrong choice")
    if marker == "#":
        return ("#","@")
    else:
        return ("@","#")

#functioon for placing the marker
def place_marker(board,marker,position,count):
    if count <= 5:
        board[position]=marker
    else:
        board[position[0]] = " "
        board[position[1]] = marker

#checking the winner

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark)) # down the right side
   
#function for choosing the player first turn

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
#function for check space is filled or not

def space_check(board, position):
    
    if not board[position] == ' ' :
        print("This is already occupied")
        return False
    else:
        return True
def full_board_check(board):
    return False
#checking rigths

def rights_check(board,player_marker,position):
    if not board[position] == player_marker:
        print('You have no rights take opponent coin')
        return False
    else:
        return True
#neighbour checking

def neightbour_check(board,position1):
    if position1 == 1:
        if not board[4] == " " and not  board[2] == " " :
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 2:
        if not board[1] == " " and not board[3] == " " and not board[5] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 3:
        if not board[2] == " " and not board[6] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 4:
        if not board[1] == " " and not board[5] == " " and not board[7] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 5:
        if not board[2] == " " and not board[4] == " " and not board[6] == " " and not board[8] == " " :
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 6:
        if not board[3] == " " and not board[5] == " " and not board[9] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 7:
        if not board[4] == " " and not board[8] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 8:
        if not board[5] == " " and not board[7] == " " and not board[9] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    elif position1 == 9:
        if not board[6] == " " and not board[8] == " ":
            print(f"{position1} is Not a Horse to Double Jump")
            return False
        else:
            return True
    else:
        return True

#taking the player choice

def player_choice(board,player_marker,count):
    position = 0
    position1 = 0
    position2 = 0
    if count <= 5:
        while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
            if position > 9:
                print("you entering out of range enter below 9")
                position = int(input('Choose your  position: (1-9) '))
            else:
                position = int(input('Choose your  position: (1-9)  '))
       
   
        
    else:
        while position1 not in [1,2,3,4,5,6,7,8,9] or position1 not in [1,2,3,4,5,6,7,8,9] or not rights_check(board,player_marker,position1) or not space_check(board,position2) or not neightbour_check(board,position1):

            if position1  > 9:
                Print('you are hight')
                
                position1,position2 =input('Enter  "From" and "To" Position ').split()
                position1=int(position1)
                position2=int(position2)
                position = [position1,position2]
            else:
                
                position1,position2 =input('Enter  "From" and "To" Position ').split()
                position1=int(position1)
                position2=int(position2)
                position = [position1,position2]
    return position

#replay function

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')






#starting the game

while True:
    #for identifying place coins or move coins
    count=0
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_marker()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_table(theBoard)
            position = player_choice(theBoard,player1_marker,count)
            place_marker(theBoard, player1_marker, position,count)
            count +=1

            if win_check(theBoard, player1_marker):
                display_table(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_table(theBoard)
            position = player_choice(theBoard,player2_marker,count)
            place_marker(theBoard, player2_marker, position,count)
            count +=1

            if win_check(theBoard, player2_marker):
                display_table(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
  
    if not replay():
        break






    
    
         
    
        
    
    
