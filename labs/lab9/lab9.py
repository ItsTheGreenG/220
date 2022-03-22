"""
Name: Owen Schlagenhaft
Lab9.py
Created a game of Tic Tack Toe!
"""
import math

def build_board():
    num_list = [1,2,3,4,5,6,7,8,9]
    print_board(num_list)
    return num_list
    pass




def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    if position > 9:
        print("Not Legal too high")
        return False
    if position < 1:
        print("Not Legal too low")
        return False
    else:
        return True



def fill_spot(board, position, character):
    if is_legal(board,position):
        board[position-1] = character
    print_board(board)
    pass

def winning_game(board):
    # Horizantal wins for x conditions
    if board[0] == "x" and board[1] == "x" and board[2] == "x":
        print("game over X wins!")
        return True
    if board[3] == "x" and board[4] == "x" and board[5] == "x":
        print("game over X wins!")
        return True
    if board[6] == "x" and board[7] == "x" and board[8] == "x":
        print("game over X wins!")
        return True
    # Vertical win condition for x
    if board[0] == "x" and board[3] == "x" and board[6] == "x":
        print("game over X wins!")
        return True
    if board[1] == "x" and board[4] == "x" and board[7] == "x":
        print("game over X wins!")
        return True
    if board[2] == "x" and board[5] == "x" and board[8] == "x":
        print("game over X wins!")
        return True
    # diagonal win condtion for x
    if board[0] == "x" and board[4] == "x" and board[8] == "x":
        print("game over X wins!")
        return True
    if board[2] == "x" and board[4] == "x" and board[6] == "x":
        print("game over X wins!")
        return True
    # Horizantal wins for o conditions
    if board[0] == "o" and board[1] == "o" and board[2] == 'o':
        print("game over o wins!")
        return True
    if board[3] == "o" and board[4] == "o" and board[5] == 'o':
        print("game over o wins!")
        return True
    if board[6] == "o" and board[7] == "o" and board[8] == 'o':
        print("game over o wins")
        return True
    # Vertical win condition for o
    if board[0] == "o" and board[3] == "o" and board[6] == 'o':
        print("game over o wins!")
        return True
    if board[1] == "o" and board[4] == "o" and board[7] == 'o':
        print("game over o wins!")
        return True
    if board[2] == "o" and board[5] == "o" and board[8] == 'o':
        print("game over o wins!")
        return True
    # diagonal win condtion for o
    if board[0] == "o" and board[4] == "o" and board[8] == 'o':
        print("game over o wins!")
        return True
    if board[2] == "o" and board[4] == "o" and board[6] == 'o':
        print("game over o wins!")
        return True
    else:
        return False


def game_over(board):
    boardstr = ''.join([str(elem) for elem in board])
    count = 0
    for i in boardstr:
        if i.isdigit():
            count += 1

    if count == 0:
        print("Cats Game")
        return True
    if count > 0:
        return False
    if winning_game(board) == True:
        print("Game Over")
        return True

    pass


def get_winner(board):
    pass


def play(board):
    while not game_over(board):
        print("player 1 enter a position to put an x\n")
        play = eval(input(":?"))
        fill_spot(board, play, "x")
        winning_game(game)
        if not game_over(board):
            print("player 2 enter a position to put an o\n")
            play2 = eval(input(":?"))
            fill_spot(board, play2, "o")
            winning_game(game)

    pass


def main():


    pass


if __name__ == '__main__':
    main()
    game = build_board()
    play(game)