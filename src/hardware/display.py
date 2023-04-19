"""Handles LED board initialization and cleanup"""
# pylint: disable=import-error
# todo: handle tests in repo
import board as pinout # todo: make sure no import errors
import neopixel
from hardware.board_display import BoardDisplay
from board_functions.board import Board

# todo: rename??
class Display:
    """Handles LED board initialization and cleanup"""

    def __init__(self, size):
        self.size = size
        self.should_exit = False

        # Initialize pixels
        self.pixels = neopixel.NeoPixel(pinout.D10, self.size, brightness=0.01, auto_write=False)
        # Initialize board
        self.board_display = BoardDisplay(Board(size), self.pixels, size)

    def __del__(self):
        """Clean up neopixel"""
        self.pixels.deinit()

    def draw(self):
        """Turn on/off all pixels"""
        self.board_display.draw_board()
        # tell the board to update itself
        self.pixels.show()

    def loop(self):
        """Drawing loop"""
        # todo: handle events

        self.draw()

        # todo: this is never true
        return self.should_exit
