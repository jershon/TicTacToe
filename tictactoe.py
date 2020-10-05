import time
import random

# define the board of tic tac toe
board = {
    '0':'0', '1':'1', '2':'2',
    '3':'3', '4':'4', '5':'5',
    '6':'6', '7':'7', '8':'8'
}

def check_board():
    global turn
    global winning
    winning = False
    win = {'O':'Bot', 'X':'Player'}
    if board['0'] == board['1'] == board['2'] or board['3'] == board['4'] == board['5'] or board['6'] == board['7'] == board['8']:
        print(win[turn] + ' won the match!')
        winning = True
    elif board['0'] == board['3'] == board['6'] or board['1'] == board['4'] == board['7'] or board['2'] == board['5'] == board['8']:
        print(win[turn] + ' won the match!')
        winning = True
    elif board['0'] == board['4'] == board['8'] or board['2'] == board['4'] == board['6']:
        print(win[turn] + ' won the match!')
        winning = True


def show_board(): # show the board of tic tac toe
    print(' ' + board['0'] + ' | ' + board['1'] + ' | ' + board['2'])
    print('---|---|---')
    print(' ' + board['3'] + ' | ' + board['4'] + ' | ' + board['5'])
    print('---|---|---')
    print(' ' + board['6'] + ' | ' + board['7'] + ' | ' + board['8'])

def first_move(): # choose who will move first? bot or player?
    global turn
    print('Choosing who will take the first turn, Patience is necessary')
    time.sleep(1.5)
    choose = random.randint(1,2)
    if choose ==1:
        print('Bot will move first !')
        turn = 'O'
    else:
        print('Player will move first !')
        turn = 'X'

first_move()

time.sleep(1.5)

show_board()

# process
options_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

for rounds in range(1, 10):
    time.sleep(1.5)
    if turn == 'O':
        print('Bot\'s turn')
        time.sleep(1.5)
        bot = int(random.choice(options_list))
        board[str(bot)] = turn
        options_list.remove(bot)   
    else:
        print('Player\'s turn')
        time.sleep(1.5)
        for options in options_list:
            print(options)
        player = input('Enter your choice based on the options above : ')
        while int(player) not in options_list:
            print('Your choice is not recognized! Please re-enter your choice!')
            for options in options_list:
                print(options)
            player = input('Enter your choice based on the options above : ')   
        board[player] = turn
        options_list.remove(int(player))

    show_board()
    check_board()

    if winning == True:
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'   
    time.sleep(1.5)
    


        
            




