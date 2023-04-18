"""Interacts with the LED board"""
import board as pinout # todo: make sure no import errors
import neopixel
from const import WIDTH, HEIGHT

# todo: same as graphical version - abstract classes in Python?

class BoardDisplay:
    """Interacts with the LED board"""
    width = 0
    height = 0
    size = 0
    board = None
    pixels = None

    def __init__(self, board, width=WIDTH, height=HEIGHT):
        # pylint: disable=line-too-long
        # pylint: disable=consider-using-f-string      
        self.width = width
        self.height = height
        self.board = board
        self.size = self.width*self.height # todo: organization

        assert board.size == self.size, 'board size ({0} does not meet given dimensions {1}x{2}'.format(board.size, width, height)

        self.pixels = neopixel.NeoPixel(pinout.D10, self.size, brightness=0.01, auto_write=False)

    def deinit(self):
        self.pixels.deinit()

    def draw_board(self):
        """Sets all the LEDs in accordance with the current data"""
        assert self.board, 'No board assigned'

        for i in range(self.size):
            if i >= len(self.board.data):
                print("index", i, "outside of data array bounds")
                return
            self.pixels[i] = self.board.data[i]
        # tell the board to update itself
        self.pixels.show()

    def fill(self, color):
        self.pixels.fill(color)
    
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