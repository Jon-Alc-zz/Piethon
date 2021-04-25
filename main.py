from board import Board
from custom_enums import Color

"""
This program randomly generates a Piet Mondrian-style display by dividing a given screen
size into cells, then randomly filling those cells with rectangles. The program continues
to fill in cells from left to right, top to bottom until there are no more cells remaining.

This program only displays once, and assumes that the given width and height for the window
are a number divisible by the given cell size. Otherwise, it won't look as clean.
"""
if __name__ == "__main__":

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    CELL_SIZE = 20
    SQUARE_BORDER = 1

    RANDOM_WIDTHS = [
        1, 1, 1, 1,
        2, 2, 2,
        3, 3,
        4, 4,
        5,
        6
    ]  # add same numbers to increase weight

    RANDOM_HEIGHTS = [
        1, 1, 1, 1, 1,
        2, 2, 2, 2,
        3, 3, 3,
        4, 4,
        5,
        6
    ]  # add same numbers to increase weight

    RANDOM_COLORS = [
        Color.RED,
        Color.BLUE,
        Color.YELLOW,
        Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE, Color.WHITE
    ]  # add same colors to increase weight

    board = Board(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE, SQUARE_BORDER)
    rect_list = board.generate_squares(RANDOM_WIDTHS, RANDOM_HEIGHTS, RANDOM_COLORS)
    board.fill(rect_list)
