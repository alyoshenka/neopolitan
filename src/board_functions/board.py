"""LED board data"""

<<<<<<< HEAD
# Todo
# pylint: disable=import-error
from board_functions.colors import ON, OFF

class Board:
    """Represents the colors for a board"""

    # pylint: disable=pointless-string-statement
=======
class Board:
    """Represents the colors for a board"""
    size = 0
    data = []
>>>>>>> main
    """
        board data:
            [ None, Red, Red, Red, None, Green, ... ]
    """

    def __init__(self, size):
<<<<<<< HEAD
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
            if(len(data) < self.size):
                data += [OFF for i in range(self.size - len(data))]
        # Cut the data so it doesn't "overflow" (even thought this does not cause errors)
        if cut_to_size:
            data = data[0:self.size]
        self.data = data

    def turn_on(self, idx, color=ON):
=======
        self.size = size     
        self.init_data()

    def init_data(self):
        """Initialize all 'lights' to 'on' (white)"""
        self.data = [(255,255,255) for i in range(self.size)]

    def turn_on(self, idx, color=(255,255,255)):
>>>>>>> main
        """Set the color of a given idx (default=white)"""
        if idx >= len(self.data):
            print('index {0} out of bounds: size = {1}'.format(idx, self.size))
            return
        self.data[idx] = color

    def turn_off(self, idx):
        """'Turn off' a given idx (set to None)"""
<<<<<<< HEAD
        # todo: what about with led board?
        self.data[idx] = OFF

    def set_color(self, idx, color):
        """Set the color of a given index"""
        self.turn_on(idx, color=color)
=======
        self.data[idx] = None

    def set_color(self, idx, color):
        """Set the color of a given index"""
        self.turn_on(idx, color=color)
>>>>>>> main
