import pygame

from .constants import BLACK_SQUARE, WHITE_SQUARE, ROWS, COLS, SQUARE_SIZE, BASE_POS_FEN, ALT_POS_FEN
from .utils import fen_decrypter

# Square class
class Square():
  def __init__(self, row, col, piece = None):
    self.row = row
    self.col = col
    self.piece = piece
    self.occupied = False

  def __str__(self):
    return f'piece: {self.piece}'

# Board class
class Board:
  def __init__(self):
    self.board = []
    self.selected_piece = None
    self.pieces = []
    self.create_board()
    self.color_to_move = 1
    self.num_of_moves = 0

  def draw(self, win):
    win.fill(BLACK_SQUARE)
    for row in range(ROWS):
      for col in range(row % 2, ROWS, 2):
        pygame.draw.rect(win, WHITE_SQUARE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    for piece in self.pieces:
      piece.draw(win)

  def clear_board(self):
    for row in self.board:
      for square in row:
        square.piece = None

  def assign_pieces_to_squares(self):
    self.clear_board()

    for row in self.board:
      for square in row:
        for piece in self.pieces:
          if piece.col == square.col and piece.row == square.row:
            square.piece = piece

  def update_board(self, pieces):
    self.pieces = pieces
    self.assign_pieces_to_squares()
    self.log_squares()

  def create_board(self):
    self.pieces, self.color_to_move, self.num_of_moves = fen_decrypter(ALT_POS_FEN)
    
    self.board = [[Square(col + 1, row + 1) for row in range(ROWS)] for col in range(COLS)]

    for row in self.board:
      for square in row:
        for piece in self.pieces:
          if piece.col == square.col and piece.row == square.row:
            square.piece = piece

  def log_squares(self):
    for row in self.board:
      for square in row:
        print(square)
        if square.piece:
          print(f'Positions it can go to: {square.piece.piece_type.calc_valid_squares(square.piece.col, square.piece.row, self.pieces)}')
