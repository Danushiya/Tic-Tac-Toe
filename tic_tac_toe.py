import tkinter as tk
from tkinter import messagebox
import random
import time

window = tk.Tk()
window.title("Tic Tac Toe")

# Create board
def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=2, width=6, bg="lightblue", command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")

create_board()

# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1
player_vs_computer = False

# Handle button clicks
def handle_click(row, col):
    global current_player

    if board[row][col] == 0:
        if current_player == 1:
            board[row][col] = "X"
            current_player = 2
            if not player_vs_computer:
                check_for_winner()
        else:
            board[row][col] = "O"
            current_player = 1

        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])

        if player_vs_computer:
            check_for_winner()
            if current_player == 2:
                window.after(1000, computer_move)

# Computer move
def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        handle_click(row, col)

# Check for a winner or a tie
def check_for_winner():
    winner = None

    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]

    if all([all(row) for row in board]) and winner is None:
        winner = "tie"

    if winner:
        declare_winner(winner)

# Declare the winner and ask to restart the game
def declare_winner(winner):
    if winner == "tie":
        message = "It's a tie!"
    else:
        message = f"Player {winner} wins!"

    answer = messagebox.askyesno("Game Over", message + " Do you want to restart the game?")

    if answer:
        reset_game()
    else:
        window.quit()

# Reset the game
def reset_game():
    global board, current_player
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            button = window.grid_slaves(row=i, column=j)[0]
            button.config(text="")
    current_player = 1

# Switch between player vs player and player vs computer modes
def switch_mode():
    global player_vs_computer
    player_vs_computer = not player_vs_computer
    reset_game()

# Add a button to switch between player vs player and player vs computer modes
mode_button = tk.Button(window, text="Switch Mode", command=switch_mode)
mode_button.grid(row=3, columnspan=3, sticky="nsew")

window.mainloop()

