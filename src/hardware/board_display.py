"""Interacts with the LED board"""

from const import WIDTH, HEIGHT

# todo: same as graphical version - abstract classes in Python?

class BoardDisplay:
    """Draws board data"""

    def __init__(self, board, pixels, size=WIDTH*HEIGHT):
        # pylint: disable=line-too-long
        # pylint: disable=consider-using-f-string      
        self.board = board  
        assert pixels, 'Neopixel library not initialized'
        self.pixels = pixels
        self.size = size # todo: organization
        assert board.size == self.size, 'board size ({0} does not meet given size ({1})'.format(board.size, size)           

    def draw_board(self):
        """Sets all the LEDs in accordance with the current data"""
        assert self.board, 'No board assigned'

        for i in range(self.size):
            if i >= len(self.board.data):
                print("index", i, "outside of data array bounds")
                return
            self.pixels[i] = self.board.data[i]

    # TODO: SET DATA TO MATCH!!
    def fill(self, color):
        # self.pixels.fill(color)
        self.board.fill(color)
    
    def fill_red(self):
        self.fill((255,0,0))
    def fill_green(self):
        self.fill((0,255,0))
    def fill_blue(self):
        self.fill((0,0,255))
    def fill_white(self):
        self.fill((255,255,255))
    def fill_blank(self):
        self.fill((0,0,0))