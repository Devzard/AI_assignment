import math

# The Tic-Tac-Toe board
board = [' '] * 9

# Possible winning combinations
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Players
human_player = 'X'
ai_player = 'O'

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    # Base cases - check for terminal states
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = ai_player
                eval_score = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = human_player
                eval_score = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
        return min_eval

# Evaluate the current state of the board
def evaluate(board):
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]]:
            if board[combination[0]] == ai_player:
                return 10
            elif board[combination[0]] == human_player:
                return -10
    return 0

# Check if there are any available moves left
def is_moves_left(board):
    return ' ' in board

# Print the Tic-Tac-Toe board
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Human player's move
def human_move():
    while True:
        move = input("Enter your move (0-8): ")
        if move.isdigit() and int(move) >= 0 and int(move) <= 8 and board[int(move)] == ' ':
            return int(move)
        else:
            print("Invalid move. Try again.")

# AI player's move
def ai_move():
    best_score = -math.inf
    best_move = -1

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = ai_player
            move_score = minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '

            if move_score > best_score:
                best_score = move_score
                best_move = i

    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while is_moves_left(board):
        # Human player's turn
        human_turn = human_move()
        board[human_turn] = human_player
        print_board(board)

        if evaluate(board) == -10:
            print("Congratulations! You won!")
            return

        if not is_moves_left(board):
            break

        # AI player's turn
        print("AI player's turn...")
        ai_turn = ai_move()
        board[ai_turn] = ai_player
        print_board(board)

        if evaluate(board) == 10:
            print("You lost! AI player won.")
            return

    print("It's a draw!")

# Start the game
play_game()
