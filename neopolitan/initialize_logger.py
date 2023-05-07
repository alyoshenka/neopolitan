"""Initialize the package logger"""

import logging
import datetime
import os

def init_logger(prep='logs/'):
    """Set up the log file"""
    # todo: prep arg validation
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

def get_logger():
    """Get the package logger"""
    return logging.getLogger('neopolitan')
