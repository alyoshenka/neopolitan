from dataclasses import dataclass

@dataclass
class BoardData: # todo: DisplayData?
    message: str
    graphical: bool
    scroll_speed: str
    scroll_wait: float
    should_wrap: bool

default_board_data = BoardData('hello world', True, 'medium', 0.2, True)
