"""LED board data"""

# Todo
# pylint: disable=import-error
from board_functions.colors import ON, OFF

class Board:
    """Represents the colors for a board"""

    # pylint: disable=pointless-string-statement
    """
        board data:
            [ None, Red, Red, Red, None, Green, ... ]
    """

    def __init__(self, size):
        self.size = size
        self.data = []
        self.init_data()

    def init_data(self):
        """Initialize all 'lights' to 'on' (white)"""
        self.data = [OFF for i in range(self.size)]

    def turn_on(self, idx, color=ON):
        """Set the color of a given idx (default=white)"""
        if idx >= len(self.data):
            print('index {0} out of bounds: size = {1}'.format(idx, self.size))
            return
        self.data[idx] = color

    def turn_off(self, idx):
        """'Turn off' a given idx (set to None)"""
        # todo: what about with led board?
        self.data[idx] = OFF

    def set_color(self, idx, color):
        """Set the color of a given index"""
        self.turn_on(idx, color=color)
