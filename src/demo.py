"""Some board demos"""

# pylint: disable=fixme
# ToDo: fix this

import getopt
import sys
<<<<<<< HEAD
import time
=======

>>>>>>> main

from board_functions.display import Display
from board_functions.board import Board
from board_functions.colors import OFF, ON
from writing.data_transformation import character_to_symbol, symbol_to_array


def main():
    """Make a very simple display"""
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches

    message = 'hello world'
    graphical = True
    scroll_speed = 'medium'
<<<<<<< HEAD
    scroll_wait = 0.2
=======
>>>>>>> main
    wrap = True
    argument_list = sys.argv[1:]
    options = 'm:g:s:w:'
    long_options = ['message=', 'graphical=', 'scroll=', 'wrap=']
    try:
        # args, vals
        args = getopt.getopt(argument_list, options, long_options)
        if len(args[0]) > 0:
            for arg, val in args[0]:
                if arg in ('-m', '--message'):
                    message = val
                elif arg in ('-g', '--graphical'):
                    if val == 'True':
                        graphical = True
                    elif val == 'False':
                        graphical = False
                    else:
                        print('Could not parse "graphical" argument:', val)
                elif arg in ('-s', 'scroll'):
                    if val in ('slow', 'medium', 'fast'):
                        scroll_speed = val
<<<<<<< HEAD
                        if scroll_speed == 'slow':
                            scroll_wait = 0.7
                        elif scroll_speed == 'medium':
                            scroll_wait = 0.2
                        else: # fast
                            scroll_wait = 0.1
=======
>>>>>>> main
                    else:
                        print('Invalid scroll speed:', val)
                elif arg in ('-w', 'wrap'):
                    if val == 'True':
                        wrap = True
                    elif val == 'False':
                        wrap = False
                    else:
                        print('Could not parse "wrap" argument:', val)
        print('message set to:', message)
        print('graphical set to:', graphical)
        print('scroll speed set to:', scroll_speed)
        print('wrap set to:', wrap)

    except getopt.error as err:
        print('getopt error:', str(err))

    width = 32
    height = 8
    size = width*height
    board = Board(size)
    display = Display(board=board)

    # Display "hello"
    space = [OFF for i in range(8)]
    concat = space
    for char in message:
        arr = symbol_to_array(character_to_symbol(char), color=ON, off=OFF)
        concat += space + space # todo: use defined space
    board.set_data(concat)

    display.init_pygame()
    while not display.should_exit:
        display.loop()
        if scroll_speed:
            board.scroll()
            
        time.sleep(scroll_wait)
