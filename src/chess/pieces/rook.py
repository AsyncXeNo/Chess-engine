import pygame
import os
import sys

# For test
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from piece import Piece
# For test


class Rook:
  def __init__(self, color, first_move = True):
    self.color = color
    self.first_move = first_move
    self.offsets = [(0, 1,), (1, 0,), (0, -1,), (-1, 0,)]
    self.max_squares = 7

  def __str__(self):
    return 'r (Rook)'

#------------------------------------------------------------------------------------------------
  def calc_valid_squares(self, col, row, pieces):
    original = (col, row,)

    valid_squares = []

    for offset in self.offsets:
      valid_for_this_offset = []
      for _ in range(self.max_squares):
        col += offset[0]
        row += offset[1]

        if not (col > 8) and not (col < 1):
          if not (row > 8) and not (row < 1):
            valid_for_this_offset.append((col, row,))
              
      col = original[0]
      row = original[1]

      for _ in range(self.max_squares):
        col += offset[0]
        row += offset[1]

        for piece in pieces:
          for square in valid_for_this_offset:
            if piece.col == square[0] and piece.row == square[1]:
              if piece.color != self.color:
                valid_for_this_offset = valid_for_this_offset[0:(valid_for_this_offset.index(square) + 1)]
                break
              else:
                valid_for_this_offset = valid_for_this_offset[0:(valid_for_this_offset.index(square))]
                break

      col = original[0]
      row = original[1]

      for square in valid_for_this_offset:
        valid_squares.append(square)

    return valid_squares
#--------------------------------------------------------------------------------

  def move(self):
    pass


"""----------------------------------------------TEST-----------------------------------------"""
# p1 = Piece(Rook(0), 5, 4, 0)
# p2 = Piece(Rook(1), 4, 3, 1)

# pieces = [p1, p2]

# p3 = Piece(Rook(1), 4, 4, 1)
# valid = p3.piece_type.calc_valid_squares(p3.col, p3.row, pieces)
# print(valid)
