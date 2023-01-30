"""Displays a graphical representation of the LED board"""

import pygame
# pylint: disable=fixme
# Todo
from board_functions.board_display import BoardDisplay

class Display:
    """A graphical LED display"""
    # pylint: disable=too-many-instance-attributes

    # pylint: disable=too-many-arguments
    def __init__(
            self, board,
            rows=8, cols=32,
            width=1600, height=400,
            background=(0, 20, 30), size=20, space=50):
        self.background = background
        self.width = width
        self.height = height
        self.board = board
        self.size = size
        self.space = space

        self.should_exit = False

        self.board_display = BoardDisplay(board, cols, rows)
        self.init_pygame()

    def init_pygame(self):
        """Initialize pygame"""
        # ToDo
        # pylint: disable=no-member
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        # pygame.display.set_caption('stock board simulator')
        # icon = pygame.image.load('./assets/images/wsb.png')
        # pygame.display.set_icon(icon)

    def draw(self):
        """Main draw loop"""
        self.screen.fill(self.background)
        self.board_display.draw_board(self.screen, self.space, self.size)

    def loop(self):
        """Loop until 'esc' or quit"""
        for event in pygame.event.get():
            # ToDo
            # pylint: disable=no-member
            if event.type == pygame.QUIT:
                self.should_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.board.turn_on(0)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.board.turn_off(0)
        self.draw()
        pygame.display.update()
        return self.should_exit
    