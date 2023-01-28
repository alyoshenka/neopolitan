"""LED board data"""

class Board:
    """Represents the colors for a board"""
    size = 0
    data = []
    """
        board data:
            [ None, Red, Red, Red, None, Green, ... ]
    """

    def __init__(self, size):
        self.size = size     
        self.init_data()

    def init_data(self):
        """Initialize all 'lights' to 'on' (white)"""
        self.data = [(255,255,255) for i in range(self.size)]

    def turn_on(self, idx, color=(255,255,255)):
        """Set the color of a given idx (default=white)"""
        if idx >= len(self.data):
            print('index {0} out of bounds: size = {1}'.format(idx, self.size))
            return
        self.data[idx] = color

    def turn_off(self, idx):
        """'Turn off' a given idx (set to None)"""
        self.data[idx] = None

    def set_color(self, idx, color):
        """Set the color of a given index"""
        self.turn_on(idx, color=color)