import pygame
from .constants import BLACK_SQUARE, WHITE_SQUARE, ROWS, COLS, SQUARE_SIZE

class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.pieces = []

  def draw(self, win):
    win.fill(BLACK_SQUARE)
    for row in range(ROWS):
      for col in range(row % 2, ROWS, 2):
        pygame.draw.rect(win, WHITE_SQUARE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
