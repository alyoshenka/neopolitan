"""Draws a board"""

import pygame
# from board import Board

class BoardDisplay:
    """Draws board data"""
    width = 0
    height = 0
    board = None

    def __init__(self, board, width, height=8):
        assert board.size == width * height, 'board size ({0} does not meet given dimensions {1}x{2}'.format(board.size, width, height)
        self.width = width
        self.height = height
        self.board = board

    def draw_board(self, screen, space, size):
        """Draw all the 'lights' in the board"""
        assert self.board, 'No board assigned'

        for i in range(self.width * self.height):
            if(i >= len(self.board.data)):
                print("index", i, "outside of data array bounds")
                return
            color = self.board.data[i]            
            row = self.get_row(i)
            col = self.get_col(i)

            if not self.board.data[i]: 
                continue
            pos = (col * space + space/2, row * space + space/2)
            pygame.draw.circle(screen, color, pos, size)

    def get_row(self, idx):
        """Gets the row # from the index"""
        return idx % self.height
    def get_col(self, idx):
        """Gets the col # from the idx"""
        return idx // self.height