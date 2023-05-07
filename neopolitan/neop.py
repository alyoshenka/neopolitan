"""Main application function"""

# pylint: disable=fixme
# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=import-outside-toplevel
# pylint: disable=logging-fstring-interpolation
# ToDo: fix this

# todo: only import pygame if on graphical

import getopt
import sys
import time
import logging
import datetime

from neopolitan.board_functions.board import Board
# from board_functions.colors import OFF, ON
from neopolitan.board_functions.board_data import default_board_data
from neopolitan.writing.data_transformation import str_to_data
from neopolitan.os_detection import on_pi
# pylint: disable=wildcard-import
from neopolitan.const import *

def initialize_logger(prep='logs/'):
    """Set up the log file"""
    # todo: prep arg validation
    import os
    # make directory if it does not exist
    # todo: is this ok?
    if not os.path.exists(prep):
        os.makedirs(prep)
    log_time = str(datetime.datetime.now()) \
        .replace(" ", "_") \
        .replace(".", "_") \
        .replace(":", "-")
    filename = f'{os.getcwd()}/{prep}neopolitan_{log_time}.txt'
    logging.basicConfig(filename=filename, encoding='utf=8', level=logging.DEBUG)

def main(events=None):
    """Make a very simple display"""

    initialize_logger()

    board_data = process_arguments()

    width = WIDTH
    height = HEIGHT
    size = width*height
    board = None
    display = None
    board_display = None

    # todo: make better
    if board_data.graphical:
        from neopolitan.display.graphical_display import GraphicalDisplay
        board = Board(size)
        display = GraphicalDisplay(board=board)
    else:
        from neopolitan.display.hardware_display import HardwareDisplay
        display = HardwareDisplay(WIDTH*HEIGHT)
        board_display = display.board_display
        board = board_display.board

    board.set_data(str_to_data(board_data.message))

    while not display.should_exit:
        # process events
        # todo: make better
        while events and not events.empty():
            event = events.get()
            logging.info(f'event: {event}')
            event_list = event.split()
            first = event_list[0]
            if first == 'exit':
                return
            if first == 'say':
                logging.info(f'say: {event}')
                # todo: better handling: this is unintuitive
                message = ' '
                for word in event_list[1:]:
                    message += word + ' '
                logging.info(message)
                board.set_data(str_to_data(message))
                logging.info(f'set message: {message}')
            else: # try board data events
                board_data = process_board_data_events(board_data, event_list)
            # todo: error handling
        display.loop()
        if board_data.scroll_speed:
            board.scroll(wrap=board_data.should_wrap)

        time.sleep(board_data.scroll_wait)

    del display

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
                        if on_pi():
                            logging.warning('This code cannot be run in graphical' \
                                            ' mode on a Raspberry Pi, setting graphical to False')
                            board_data.graphical = False
                        else:
                            board_data.graphical = True
                    elif val == 'False':
                        if not on_pi():
                            logging.warning('This code cannot be run in hardware mode when not run'\
                            ' on a Raspberry Pi, setting graphical to True')
                            board_data.graphical = True
                        else:
                            board_data.graphical = False
                    else:
                        logging.warning(f'Could not parse "graphical" argument: {val}')
                elif arg in ('-s', 'scroll'):
                    if val in ('slow', 'medium', 'fast'):
                        board_data.scroll_speed = val
                        if val == 'slow':
                            board_data.scroll_wait = SCROLL_FAST
                        elif val == 'medium':
                            board_data.scroll_wait = SCROLL_MED
                        else: # fast
                            board_data.scroll_wait = SCROLL_SLOW
                    else:
                        logging.warning(f'Invalid scroll speed: {val}')
                elif arg in ('-w', 'wrap'):
                    if val == 'True':
                        board_data.should_wrap = True
                    elif val == 'False':
                        board_data.should_wrap = False
                    else:
                        logging.warning(f'Could not parse "wrap" argument: {val}')
        logging.info(f'message set to: {board_data.message}')
        logging.info(f'graphical set to: {board_data.graphical}')
        logging.info(f'scroll speed set to: {board_data.scroll_speed} ({board_data.scroll_wait})')
        logging.info(f'wrap set to: {board_data.should_wrap}')

    except getopt.error as err:
        logging.error(f'getopt error: {err}')

    return board_data

def process_board_data_events(board_data, event_list):
    """Manipulate board data according to events"""
    
    first = event_list[0]
    if first == 'speed':
        try:
            speed = event_list[1]
        # pylint: disable=broad-except
        except Exception as err:
            # todo: better explanation
            logging.warning('No second value provided, %s', err)
        if speed == 'slow':
            board_data.scroll_slow()
            logging.info('set speed: slow')
        elif speed == 'medium':
            board_data.scroll_medium()
            logging.info('set speed: medium')
        elif speed == 'fast':
            board_data.scroll_fast()
            logging.info('set speed: fast')
        else:
            try:
                speed = float(speed)
                board_data.set_scroll_wait(speed)
                logging.info(f'set speed: {speed}')
            except ValueError:
                logging.warning(f'Cannot parse speed: {speed}')
    elif first == 'wrap':
        try:
            wrap = event_list[1]
        # pylint: disable=broad-except
        except Exception as err:
            # todo: better explanation
            logging.warning('No second value provided, %s', err)
        if wrap in ('True', '1'):
            board_data.should_wrap = True
            logging.info('set wrap: True')
        elif wrap in ('False', '0'):
            board_data.should_wrap = False
            logging.info('set wrap: False')
        else:
            logging.warning('Cannot parse wrap: %s', wrap)

    return board_data

if __name__ == '__main__':
    main()
