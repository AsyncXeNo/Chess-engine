import pygame
from .constants import BLACK_SQUARE, WHITE_SQUARE, ROWS, COLS, SQUARE_SIZE, BASE_POS_FEN, ALT_POS_FEN
from .utils import fen_decrypter

class Square():
  def __init__(self, row, col):
    self.row = row
    self.col = col
    self.occupied = False

  def __str__(self):
    return f'<{self.col}, {self.row}>'

class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.pieces = []
    self.create_board()

  def draw(self, win):
    win.fill(BLACK_SQUARE)
    for row in range(ROWS):
      for col in range(row % 2, ROWS, 2):
        pygame.draw.rect(win, WHITE_SQUARE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for piece in self.pieces:
      piece.draw(win)

  def create_board(self):
    self.pieces = fen_decrypter(ALT_POS_FEN)
    self.board = [[Square(col + 1, row + 1) for row in range(ROWS)] for col in range(COLS)]

    # delete
    # for row in self.board:
    #   for square in row:
    #     print(square)

    # for piece in self.pieces:
    #   print(piece)
    # delete
