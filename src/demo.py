"""Some board demos"""

# pylint: disable=fixme
# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# ToDo: fix this

# todo: only import pygame if on graphical

import getopt
import sys
import time

from graphical.display import Display
from board_functions.board import Board
from board_functions.colors import OFF, ON
from board_functions.board_data import default_board_data
from writing.data_transformation import character_to_symbol, symbol_to_array, str_to_data
from const import WIDTH, HEIGHT


def main():
    """Make a very simple display"""
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches

    message = 'hello world'
    graphical = True
    scroll_speed = 'medium'
    scroll_wait = 0.2
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
                        if scroll_speed == 'slow':
                            scroll_wait = 0.7
                        elif scroll_speed == 'medium':
                            scroll_wait = 0.2
                        else: # fast
                            scroll_wait = 0.1
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
        concat = concat + space + arr # todo: use defined space
    board.set_data(concat)

    display.init_pygame()
    while not display.should_exit:
        display.loop()
        if scroll_speed:
            board.scroll(wrap=wrap)

        time.sleep(scroll_wait)

def process_arguments():
    """Process the command line arguments and return them as a BoardData object"""
    board_data = default_board_data

    argument_list = sys.argv[1:]
    options = 'm:g:s:w:'
    long_options = ['message=', 'graphical=', 'scroll=', 'wrap=']
    try:
        # args, vals
        args = getopt.getopt(argument_list, options, long_options)
        if len(args[0]) > 0:
            for arg, val in args[0]:
                if arg in ('-m', '--message'):
                    board_data.message = val
                elif arg in ('-g', '--graphical'):
                    if val == 'True':
                        board_data.graphical = True
                    elif val == 'False':
                        board_data.graphical = False
                    else:
                        print('Could not parse "graphical" argument:', val)
                elif arg in ('-s', 'scroll'):
                    if val in ('slow', 'medium', 'fast'):
                        board_data.scroll_speed = val
                        if val == 'slow':
                            board_data.scroll_wait = 0.7
                        elif val == 'medium':
                            board_data.scroll_wait = 0.2
                        else: # fast
                            board_data.scroll_wait = 0.1
                    else:
                        print('Invalid scroll speed:', val)
                elif arg in ('-w', 'wrap'):
                    if val == 'True':
                        board_data.should_wrap = True
                    elif val == 'False':
                        board_data.should_wrap = False
                    else:
                        print('Could not parse "wrap" argument:', val)
        print('message set to:', board_data.message)
        print('graphical set to:', board_data.graphical)
        print(f'scroll speed set to: {board_data.scroll_speed} ({board_data.scroll_wait})')
        print('wrap set to:', board_data.should_wrap)

    except getopt.error as err:
        print('getopt error:', str(err))

    return board_data

def with_args(events):
    """Make a very simple display, includes event queue as an argument"""
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-branches

    board_data = process_arguments()

    width = WIDTH
    height = HEIGHT
    size = width*height
    board = Board(size)
    display = Display(board=board)

    # Display "hello"
    board.set_data(str_to_data(board_data.message))

    # todo: graphical?

    display.init_pygame()
    while not display.should_exit:
        # process events
        # todo: make better
        while not events.empty():
            event = events.get()
            print('event:', event)
            event_list = event.split()
            first = event_list[0]
            if first == 'exit':
                return
            if first == 'say':
                print('e:', event)
                message = event_list[1]
                board.set_data(str_to_data(message))
                print('set message:', message)
            # todo: error handling

        display.loop()
        if board_data.scroll_speed:
            board.scroll(wrap=board_data.should_wrap)

        time.sleep(board_data.scroll_wait)

def on_board():
    """Run operations on the board"""
    # todo: make absolutely sure this is running on the Pi
    # (or something that can handle the required libraries)

    # pylint: disable=redefined-outer-name
    # pylint: disable=import-outside-toplevel
    from hardware.display import Display as HardwareDisplay

    board_data = process_arguments()

    display = HardwareDisplay(WIDTH*HEIGHT)
    board_display = display.board_display
    board = board_display.board
    slp = 0.5

    display.draw()
    time.sleep(slp)
    board_display.fill((255,0,0))
    display.draw()
    time.sleep(slp)
    board_display.fill((0,255,0))
    display.draw()
    time.sleep(slp)
    board_display.fill((0,0,255))
    display.draw()
    time.sleep(slp)
    board_display.fill((255,255,255))
    display.draw()
    time.sleep(slp)

    board.set_data(str_to_data(board_data.message))
    while not display.should_exit:
        display.loop()
        if board_data.scroll_speed:
            board.scroll(wrap=board_data.should_wrap)

        time.sleep(board_data.scroll_wait)

    display.deinit()
    