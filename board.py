from window import Window
from random import choice


class Board:

    def __init__(self, width, height, cell_size, border):
        self.__board_width = width
        self.__board_height = height
        self.__cell_size = cell_size
        self.__board = [
            [False for i in range(self.__board_width // self.__cell_size)]
            for j in range(self.__board_height // self.__cell_size)
        ]
        self.window = Window(width, height, border)

    def generate_squares(self, widths, heights, colors):
        entries = list()
        for row in range(len(self.__board)):  # for each row in board
            for col in range(len(self.__board[row])):  # for each column (position in row) in board
                if not self.__board[row][col]:  # if this space isn't already filled
                    entries.append(self.__gen_helper(widths, heights, colors, row, col))  # make a rect starting here

        return entries

    # __gen_helper generates and returns parameters to draw a rectangle
    # - also checks if the size picked is legal (no rectangles blocking, is within bounds)
    def __gen_helper(self, widths, heights, colors, row, col):

        new_width = choice(widths)
        new_height = choice(heights)
        new_color = choice(colors)
        self.__board[row][col] = True  # then set this space to True since it's filled

        # verify new_width doesn't overlap with other rectangles
        for i in range(1, new_width):
            if col + i >= len(self.__board[0]) or self.__board[row][col + i]:
                new_width = i
                break

        for i in range(1, new_height):
            if row + i >= len(self.__board) or self.__board[row + i][col]:
                new_height = i
                break

        for i in range(new_width):
            for j in range(new_height):
                self.__board[row + j][col + i] = True

        return new_color, (col, row), (new_width, new_height)

    # rect_list is a list of tuples containing:
    # [0] = inner_color: Color, color of square
    # [1] = start: tuple, x and y coordinates of top left corner
    # [2] = dimensions: tuple, width and height of the rectangle
    def fill(self, rect_list: list):
        for rect in rect_list:
            self.window.draw_rect(
                rect[0],
                self.__cell_size * rect[1][0],
                self.__cell_size * rect[1][1],
                self.__cell_size * rect[2][0],
                self.__cell_size * rect[2][1]
            )
        self.window.run()
