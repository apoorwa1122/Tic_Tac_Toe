import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Dynamic GUI")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.label = tk.Label(self.root, text=f"Turn: Player {self.current_player}", font=("Arial", 16), fg="blue")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", width=10, height=3, font=("Arial", 20), 
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, disabledforeground="black", state="disabled")
            
            if self.check_win():
                self.label.config(text=f"Player {self.current_player} wins!", fg="green")
                self.end_game()
            elif "" not in self.board:
                self.label.config(text="It's a Draw!", fg="orange")
                self.end_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Turn: Player {self.current_player}")

    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def end_game(self):
        for btn in self.buttons:
            btn.config(state="disabled")

        restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 14), command=self.restart)
        restart_btn.grid(row=4, column=0, columnspan=3, pady=10)

    def restart(self):
        self.current_player = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state="normal")
        self.label.config(text=f"Turn: Player {self.current_player}", fg="blue")

# Run the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
