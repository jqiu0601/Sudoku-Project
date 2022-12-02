
#This class represents an entire Sudoku board. A Board object has 81 Cell objects.
import sudoku_generator
sudo = sudoku_generator.SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        pass

    def select(self, row, col):
        # Marks the cell at(row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        self.row = row
        self.col = col
        pass

    def click(self, x, y):
        # If a tuple of(x, y) coordinates is within the displayed board, this function
        # returns a tuple of the(row, col) of the cell which was clicked. Otherwise,
        # this function returns None.
        pass

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and
        # sketched value that are filled by themselves.
        sudo.board[self.row][self.col] = 0
            

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed in the top left corner of the cell using the draw() function.
        pass # Jake's note: I'm setting all things supposed to be blank spaces to 0 which I think was in the instructions, if not then just note that.

    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        pass

    def reset_to_original(self):
        # Reset all cells in the board to their original values
        # (0 if cleared, otherwise the corresponding digit).
        pass

    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for i in sudo.board:
          for j in sudo.board[i]:
              if sudo.board[i][j] == 0:
                return False
        return True
          
    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        pass

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for i in sudo.board:
            for j in sudo.board[i]
                if sudo.board[i][j] == 0:
                    return (j + 1, i + 1)

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        if sudo.board == user_board:
          win = True
          # win as a variable can be renamed, just the win condition.





