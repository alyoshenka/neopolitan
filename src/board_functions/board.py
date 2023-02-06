"""LED board data"""

# pylint: disable=fixme
from .colors import ON, OFF

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
        """Initialize all 'lights' to 'off' (gray)"""
        self.data = [OFF for i in range(self.size)]

    def set_data(self, data, pad_to_end=True, cut_to_size=False):
        """Sets the board data and optionally makes it the right length"""

        # Pad the data so it fills the whole size
        if pad_to_end:
            if len(data) < self.size:
                data += [OFF for i in range(self.size - len(data))]
        # Cut the data so it doesn't "overflow" (even thought this does not cause errors)
        if cut_to_size:
            data = data[0:self.size]
        self.data = data

    def turn_on(self, idx, color=ON):
        """Set the color of a given idx (default=white)"""
        if idx >= len(self.data):
            # pylint: disable=consider-using-f-string
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

    def scroll(self, wrap=True, height=8):
        """'Scrolls' the data by one 'column' (height)"""
        to_remove = self.data[0:height]
        self.data = self.data[height:]
        if wrap:
            self.data += to_remove
            
