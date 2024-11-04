import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        """
        Initialize the Tic Tac Toe game with a GUI.
        """
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.configure(bg='light blue')  # Set background color to light blue

        # Initialize game state
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Start with player 'X'

        # Create a frame to center the buttons
        self.frame = tk.Frame(root, bg='light blue')
        self.frame.grid(row=1, column=1, padx=50, pady=50)  # Adjust padding for centering

        # Create buttons for the board with larger size
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.frame, text=' ', font=('Arial', 40), width=5, height=2,
                               bg='blue', fg='white',  # Button background and text color
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i//3, column=i%3, padx=5, pady=5)  # Adding padding for spacing
            self.buttons.append(button)

    def make_move(self, index):
        """
        Handle a player's move on the board.
        """
        if self.board[index] == ' ':
            # Mark the board and update the button text
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            # Check for a win or draw
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch players
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, player):
        """
        Check if the current player has won.
        """
        # Winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)             # diagonals
        ]

        # Check if any winning combination is met
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True

        return False

    def check_draw(self):
        """
        Check if the game is a draw.
        """
        return ' ' not in self.board

    def reset_game(self):
        """
        Reset the game board and variables.
        """
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text=' ')

# Main function to run the game
import main():
    # Create the main window
    root = tk.Tk()

    # Set the window size
    root.geometry('500x550')  # Adjusted window size for better centering

    # Create an instance of the Tic Tac Toe game
    game = TicTacToe(root)

    # Configure grid to center the frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(2, weight=1)

    # Run the GUI event loop
    root.mainloop()

# Start the game
if __name__ == "__main__":
    main()



