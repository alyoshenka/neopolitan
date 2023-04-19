"""Holds data for displaying a board"""
from dataclasses import dataclass

@dataclass
class BoardData: # todo: DisplayData?
    """Holds data for displaying a board"""
    message: str
    graphical: bool
    scroll_speed: str
    scroll_wait: float
    should_wrap: bool

default_board_data = BoardData('hello world', False, 'medium', 0.2, True)
