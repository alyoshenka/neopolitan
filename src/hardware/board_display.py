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

        flipped_data = BoardDisplay.flip(self.board.data, HEIGHT)

        for i in range(self.size):
            if i >= len(self.board.data):
                print("index", i, "outside of data array bounds")
                return
            self.pixels[i] = flipped_data[i]

    def flip(data, height=HEIGHT, startAtFirst=False):
        """Handles flipping alternate 'rows' so that data appears as expected; returns the flipped data"""

        # Every other 'column', starting with the second, should be flipped such that it appears 'upside down', so that when the board displays it actually appears right side up.
        assert len(data) % height == 0, 'Data length does not fill its last column' # todo: doesn't need to tho

        flipped_data = []
        idx = 0
        while idx < len(data):
            col = data[idx:idx+height]
            if startAtFirst:
                col = reversed(col)
            startAtFirst = not startAtFirst
            flipped_data += col
            idx += height

        return flipped_data

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