#Task 6
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    # Class variable
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    def __init__(self):
        # Create a 3x3 board filled with spaces
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"  # X always goes first

        class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Board:
    valid_moves = [
        "upper left", "upper center", "upper right",
        "middle left", "center", "middle right",
        "lower left", "lower center", "lower right"
    ]

    move_mapping = {
        "upper left": (0, 0),
        "upper center": (0, 1),
        "upper right": (0, 2),
        "middle left": (1, 0),
        "center": (1, 1),
        "middle right": (1, 2),
        "lower left": (2, 0),
        "lower center": (2, 1),
        "lower right": (2, 2)
    }

    def __init__(self):
        self.board_array = [[" " for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.last_move = None

    def __str__(self):
        rows = []
        for row in self.board_array:
            rows.append(" | ".join(row))
        return f"\n---------\n".join(rows)

    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")

        row, col = Board.move_mapping[move_string]

        if self.board_array[row][col] != " ":
            raise TictactoeException("That spot is taken.")

        self.board_array[row][col] = self.turn
        self.last_move = (row, col)
        self.turn = "O" if self.turn == "X" else "X"

    def whats_next(self):
        # Check rows, columns, and diagonals for a winner
        lines = []

        # Rows and Columns
        for i in range(3):
            lines.append(self.board_array[i])  # Row
            lines.append([self.board_array[0][i], self.board_array[1][i], self.board_array[2][i]])  # Column

        # Diagonals
        lines.append([self.board_array[0][0], self.board_array[1][1], self.board_array[2][2]])
        lines.append([self.board_array[0][2], self.board_array[1][1], self.board_array[2][0]])

        for line in lines:
            if line == ["X", "X", "X"]:
                return (True, "X has won")
            elif line == ["O", "O", "O"]:
                return (True, "O has won")

        # Check for draw
        if all(cell != " " for row in self.board_array for cell in row):
            return (True, "Cat's Game")

        # Game not over
        return (False, f"{self.turn}'s turn")


# Game loop
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    board = Board()

    while True:
        print("\nCurrent board:")
        print(board)
        print(f"\n{board.turn}'s turn.")

        move = input("Enter your move: ").strip().lower()

        try:
            board.move(move)
        except TictactoeException as e:
            print(f"Error: {e.message}")
            continue

        game_over, message = board.whats_next()
        if game_over:
            print("\nFinal board:")
            print(board)
            print("\nGame Over -", message)
            break