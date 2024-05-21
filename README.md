# Tic-Tac-Toe Game

Welcome to the Tic Tac Toe game, a simple and fun application implemented using Python's Tkinter library.

This game can be played in two modes: **Player vs Player** and **Player vs Computer**.

## Features

- **Two Modes:** Play against another player or challenge the computer.
- **Intuitive Interface:** User-friendly design with a clickable grid.
- **Automatic Restart:** Option to restart the game after a win or a tie.
- **Randomized Computer Moves:** The computer opponent makes random valid moves.

## Screenshots

![Screenshot 1](/images/ticplyr.png) ![Screenshot 2](/images/ticcomp.png)

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python standard library)

## Installation

No installation is required. Simply download the script and run it using Python.

## How to Run
1. Ensure you have Python installed on your system.
2. Save the script to a file named **'tic_tac_toe.py'**.
3. Open your terminal or command prompt.
4. Navigate to the directory where the script is saved.
5. Run the script with the command:

    ***python tic_tac_toe.py***
   
## Gameplay

### Player vs Player Mode

1. The game starts with Player 1 ('X').
2. Players take turns clicking on the grid to place their marks.
3. The first player to align three marks horizontally, vertically, or diagonally wins.
4. If the grid is filled without a winner, the game ends in a tie.

### Player vs Computer Mode

1. Click the **"Switch Mode"** button to enable Player vs Computer mode.
2. Player 1 ('X') makes the first move.
3. The computer ('O') will make random valid moves after Player 1's turn.
4. The game follows the same winning and tie conditions as the Player vs Player mode.

## Code Explanation

- **Board Creation:** A 3x3 grid of buttons is created using Tkinter.
- **Button Click Handling:** The handle_click function updates the board state and switches the turn between players or the computer.
- **Computer Moves:** The computer_move function makes random moves on behalf of the computer.
- **Win/Tie Check:** The check_for_winner function checks for a winning condition or a tie.
- **Winner Declaration:** The declare_winner function shows a message box with the game result and prompts to restart or quit.
- **Game Reset:** The reset_game function clears the board and resets the state.
- **Mode Switch:** The switch_mode button toggles between Player vs Player and Player vs Computer modes and resets the game.

## File Structure

The project consists of a single script file:

- **tic_tac_toe.py**: Contains the complete code for the game.
