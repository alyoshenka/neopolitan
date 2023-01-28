"""
Main
"""

import time

# ToDo: fix this
# pylint: disable=import-error
from board_functions.display import Display
from board_functions.board import Board

def show_display():
    """Make a very simple display"""
    w = 32
    h = 8
    s = w*h
    board = Board(s)
    display = Display(board=board)
    display.init_pygame()
    while not display.should_exit:
        display.loop()


def main():
    """Main entry point of the program"""
    print('hello neopolitan')

    show_display()

if __name__ == '__main__':
    main()
    