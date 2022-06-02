#unbeatable tic tac toe game 


board = {1:' ', 2:' ', 3:' ' , 4:' ' , 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
player = 'o'
bot = 'x'


#draw the board on the output screen
def draw_board(board):                                  
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


#check if the given space which is entered is free
def FreeSapce(position):
    if board[position] == ' ':
        return True
    else:
        return False


#checks if the condition for winning is satisfied
def win_check():
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[3] != ' ':
        return True
    else:
        False


#checks which mark/player won o or x
def check_which_mark_won(mark):
    if board[1] == board[2] and board[2] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[1] == mark:
        return True
    elif board[3] == board[5] and board[5] == board[7] and board[3] == mark:
        return True
    else:
        False



#checks if the given game is a 
def Draw_check():
    for keys in board.keys():
        if board[keys] == ' ':
            return False
    return True

def Enter_pos(letter, position):
    if FreeSapce(position):
        board[position] = letter
        draw_board(board)
        if Draw_check():
            print('The game is a draw')


        if win_check():
            if letter == 'x':
                print('YOU LOSE')
                exit()
            else:
                print('YOU WIN')
                exit()
        return 
    else:
        print('Can\'nt place there')
        position = int(input('Enter your position'))
        Enter_pos(letter, position)
        return 

def player_move():
    position = int(input('Enter the position of o: '))
    Enter_pos(player, position)
    return

def comp_move():
    bestScore = float('-inf')
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if(score > bestScore):
                bestScore = score
                bestMove = key 

    Enter_pos(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):

    if check_which_mark_won(bot):
        return 1                                                #this assign the scores for the minmax algorithm
    elif check_which_mark_won(player):
        return -1
    elif Draw_check():
        return 0
    if isMaximizing:
        bestScore = -1000

        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    

    else:
        bestScore = 800

        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
         



while not win_check() and not Draw_check():
    player_move()
    if not win_check() and not Draw_check():
        comp_move()