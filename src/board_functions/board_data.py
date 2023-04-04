# pylint: disable=import-error
from dataclass import dataclass

@dataclass
class BoardData:
    message: str
    graphical: bool
    # don't really need scroll speed
    scroll_wait: float
    should_wrap: bool

default_board_data = BoardData('hello world', True, 0.2, True)
