# def display_board(board):
#     """
#     Function to display the Tic Tac Toe board.
#     """
#     print(board[0] + ' | ' + board[1] + ' | ' + board[2])
#     print('--|---|--')
#     print(board[3] + ' | ' + board[4] + ' | ' + board[5])
#     print('--|---|--')
#     print(board[6] + ' | ' + board[7] + ' | ' + board[8])


# def player_input(player):
#     """
#     Function to get the position from the player.
#     """
#     position = int(input(f"Player {player}, enter your position (1-9): ")) - 1
#     return position


# def check_win(board, player):
#     """
#     Function to check whether there is a winner or not.
#     """
#     win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
#                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
#                       (0, 4, 8), (2, 4, 6)]

#     for condition in win_conditions:
#         if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
#             return True
#     return False


# def play():
#     """
#     The main function, which calls all the functions created above.
#     """
#     board = [' ' for _ in range(9)]
#     current_player = 'X'

#     while True:
#         display_board(board)
#         position = player_input(current_player)

#         if board[position] == ' ':
#             board[position] = current_player

#             if check_win(board, current_player):
#                 print(f"Player {current_player} wins!")
#                 display_board(board)
#                 break

#             if ' ' not in board:
#                 print("It's a tie!")
#                 display_board(board)
#                 break

#             current_player = 'O' if current_player == 'X' else 'X'
#         else:
#             print("That position is already taken. Try again.")

# play()
