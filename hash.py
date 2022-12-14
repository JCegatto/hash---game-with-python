from IPython.display import clear_output
from random import randint

def choice ():
#Player 1 choose a simbol to start

    while True:
        symb = str(input('Choose between X or O for the player 1: ')).upper()
        if symb == 'X':
            symbol = ('X', 'O')
            break
        elif symb == 'O':
            symbol = ('O', 'X')
            break
        else:
            print ('Invalid symbol.')
            
    return symbol

def player1 (board):
#Takes player 1's movement and puts it on a list.

    while True:
        position = int(input('Choose a position player 1 wants to play [1, 9]: '))
        if position<1:
            print ('Invalid move, try again.')
        elif board[position-1] == ' ':
            board[position-1] = p1
            break
        else:
            print ('Invalid move, try again.')

def player2 (board):
#Takes player 2's movement and puts it on a list.

    while True:
        position = int(input('Choose a position player 2 wants to play [1, 9]: '))
        if position<1:
            print ('Invalid move, try again.')
        elif board[position-1] == ' ':
            board[position-1] = p2
            break
        else:
            print ('Invalid move, try again.')

def  print_board(board):
#Show the board.
    
    clear_output()
    print (f'{board[0]} | {board[1]} | {board[2]}')
    print ('-'*9)
    print (f'{board[3]} | {board[4]} | {board[5]}')
    print ('-'*9)
    print (f'{board[6]} | {board[7]} | {board[8]}')
    
    pass

def check(board, p1):
#Check the game result.

    if board[0]==board[3]==board[6]!=' ':
        if board[0] == p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[1]==board[4]==board[7]!=' ':
        if board[1] == p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[2]==board[5]==board[8]!=' ':
        if board[2]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[0]==board[1]==board[2]!=' ':
        if board[0]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[3]==board[4]==board[5]!=' ':
        if board[3]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[6]==board[7]==board[8]!=' ':
        if board[6]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[0]==board[4]==board[8]!=' ':
        if board[0]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif board[2]==board[4]==board[6]!=' ':
        if board[2]==p1:
            print ('Player 1 win!')
        else:
            print ('Player 2 win!')
        return True
    elif ' ' not in board:
        print ('Tied!')
        return True
    else:
        return False

p1, p2 = choice()    
first = randint(1, 2)
print (f'Player {first} start.')
board=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

while True:
    try:
        if first == 1:
            player1(board)
        else:
            player2(board)
        print_board(board)
        if check(board, p1):
            break
        if first == 1:
            player2(board)
        else:
            player1(board)
        print_board(board)
        if  check(board, p1):
            break
        
    except:
        print('Invalid move, try again.')
