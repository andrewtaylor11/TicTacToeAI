#Represent the board
def new_board():
        return [["~", "~", "~"], ["~", "~", "~"], ["~", "~", "~"]]

#Render the board
def render(my_board):
        print('  0 1 2')
        print('  ------')
        print('0|'+ str(my_board[0][0]) + ' ' + str(my_board[1][0]) + '  ' + str(my_board[2][0]))
        print('1|'+ str(my_board[0][1]) + ' ' + str(my_board[1][1]) + '  ' + str(my_board[2][1]))
        print('2|'+ str(my_board[0][2]) + ' ' + str(my_board[1][2]) + '  ' + str(my_board[2][2]))

#Determine which player is to go
def player(counter):
     if counter % 2 == 0:
          return 'X'
     else:
          return 'Y'
     
#Ask the player for input
def get_move():
    x_coord = int(input("What is the X coordinate of your move?"))
    y_coord = int(input("What is the Y coordinate of your move?"))
    return x_coord, y_coord

#Make a move
def make_move(old_board, move_coordinates, player):
    old_board[move_coordinates[0]][move_coordinates[1]] = player

    
#Check if there is a winner
def get_winner(old_board):
    # check the columns
    for i in range(3):
            if old_board[i][0] ==  'X' and old_board[i][1] ==  'X' and old_board[i][2] == 'X':
                print("Player X wins!")
                return True 
            if old_board[i][0] ==  'Y' and old_board[i][1] ==  'Y' and old_board[i][2] == 'Y':
                print("Player Y wins!")
                return True 
    for j in range(3):
            if old_board[0][j] ==  'X' and old_board[1][j] ==  'X' and old_board[2][j] == 'X':
                print("Player X wins!")
                return True 
            if old_board[0][j] ==  'Y' and old_board[1][j] ==  'Y' and old_board[2][j] == 'Y':
                print("Player Y wins!")
                return True 
    # check the diagonals
    if old_board[0][0] ==  'X' and old_board[1][1] ==  'X' and old_board[2][2] == 'X':
        print("Player X wins!")
        return True 
    if old_board[0][2] ==  'X' and old_board[1][1] ==  'X' and old_board[2][0] == 'X':
        print("Player X wins!")
        return True 
    if old_board[0][0] ==  'Y' and old_board[1][1] ==  'Y' and old_board[2][2] == 'Y':
        print("Player Y wins!")
        return True 
    if old_board[0][2] ==  'Y' and old_board[1][1] ==  'Y' and old_board[2][0] == 'Y':
        print("Player Y wins!")
        return True 
    return False

# This is just old test code
#board = new_board()
#board[0][0] = 'X'
#board[2][2] = 'X'
#render(board)

#move_coords = get_move()
#print(move_coords)
#x_player = 'X'
#player_turn = 'X'
#make_move(board, move_coords, player_turn)
#render(board)
#get_winner(board)

def main():
     game_turn = 0
     board = new_board()
     render(board)
     while not get_winner(board):
          move_coords = get_move()
          make_move(board, move_coords, player(game_turn))
          render(board)
          game_turn += 1

main()
