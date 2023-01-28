"""Some board demos"""

# ToDo: fix this
# pylint: disable=import-error
from board_functions.display import Display
from board_functions.board import Board

from writing.data_transformation import character_to_symbol, symbol_to_array

from board_functions.colors import OFF, ON


def show_display():
    """Make a very simple display"""
    w = 32
    h = 8
    s = w*h
    board = Board(s)
    display = Display(board=board)

    # Display "hello"
    space = [OFF for i in range(8)]
    concat = space
    for char in 'hello':
        arr = symbol_to_array(character_to_symbol(char), color=ON, off=OFF)
        concat = concat + arr + space
    board.set_data(concat)

    display.init_pygame()
    while not display.should_exit:
        display.loop()