"""Holds data for displaying a board"""
from dataclasses import dataclass
from const import SCROLL_SLOW, SCROLL_MED, SCROLL_FAST

@dataclass
class BoardData: # todo: DisplayData?
    """Holds data for displaying a board"""
    message: str
    graphical: bool
    scroll_speed: str
    scroll_wait: float
    should_wrap: bool

    def scroll_fast(self):
        self.scroll_speed = 'fast'
        self.scroll_wait = SCROLL_FAST
    
    def scroll_medium(self):
        self.scroll_speed = 'medium'
        self.scroll_wait = SCROLL_MED
    
    def scroll_slow(self):
        self.scroll_speed = 'slow'
        self.scroll_wait = SCROLL_SLOW

    def set_scroll_wait(self, timer):
        assert type(timer) == float
        self.scroll_wait = timer
        self.scroll_speed = 'user-defined'

default_board_data = BoardData('hello world', False, 'medium', 0.2, True)
