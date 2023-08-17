#Represent the board
def new_board():
        return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def render(my_board):
        print('  0 1 2')
        print('  ------')
        print('0|'+ str(my_board[0][0]) + str(my_board[1][0]) + str(my_board[2][0]))
        print('1|'+ str(my_board[0][1]) + str(my_board[1][1]) + str(my_board[2][1]))
        print('2|'+ str(my_board[0][2]) + str(my_board[1][2]) + str(my_board[2][2]))

board = new_board()
render(board)