import pygame
import copy
import os, sys

# For test
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from piece import Piece
# For test


class Pawn:

  def __init__(self, color, can_be_en_passant = False):
    self.color = color
    self.can_be_en_passant = can_be_en_passant
    self.first_move = True
    self.max_squares = 1

  def __str__(self):
    return 'p (Pawn)'

  def calc_first_move(self, row):
    self.first_move = row == (2 if self.color else 7)

  def calc_offsets(self):
    if self.first_move:
      if self.color == 1:
        self.offsets = [(0, 1,), (0, 2,)]
        self.capture_offsets = [(-1, 1,), (1, 1,)]
      else:
        self.offsets = [(0, -1,), (0, -2,)]
        self.capture_offsets = [(-1, -1,), (1, -1,)]
    else:
      if self.color == 1:
        self.offsets = [(0, 1,)]
        self.capture_offsets = [(-1, 1,), (1, 1,)]
      else:
        self.offsets = [(0, -1,)]
        self.capture_offsets = [(-1, -1,), (1, -1,)]


#--------------------------------------------------------------------------------------------------------------------------
  def calc_valid_squares(self, col, row, pieces):
    self.calc_first_move(row)
    self.calc_offsets()
    original = (col, row,)

    valid_squares = []

    for offset in self.offsets:
      for _ in range(self.max_squares):
        col += offset[0]
        row += offset[1]
        if not (col > 8) and not (col < 1):
          if not (row > 8) and not (row < 1):
            valid_squares.append((col, row,))
      
      col = original[0]
      row = original[1]

    for piece in pieces:
      if piece.color != self.color:

        if self.color == 1:
          if piece.col == col and (piece.row - 1) == row:
            valid_squares.remove((piece.col, piece.row,))

        if self.color == 0:
          if piece.col == col and (piece.row + 1) == row:
            valid_squares.remove((piece.col, piece.row,))

        if piece.piece_type.__str__()[0] == self.__str__()[0]:
          if piece.piece_type.can_be_en_passant:
            virtual_pawn = copy.copy(piece)
            if virtual_pawn.color == 1:
              virtual_pawn.row -= 1
            else:
              virtual_pawn.row += 1
            virtual_pawn.can_be_en_passent = False

    pieces.append(virtual_pawn)
            
    for piece in pieces:
      if piece.color != self.color:

        for offset in self.capture_offsets:
          for _ in range(self.max_squares):
            col += offset[0]
            row += offset[0]
            if not (col > 8) and not (col < 1):
              if not (row > 8) and not (row < 1):
                if piece.col == col and piece.row == row:
                  valid_squares.append((col, row,))  

          col = original[0]
          row = original[1] 
          
          

    for piece in pieces:
      if piece.color == self.color:
        for square in valid_squares:
          if piece.col == square[0] and piece.row == square[1]:
            valid_square.remove(square)

    return valid_squares
#----------------------------------------------------------------------------------------------------------
  def move(self):
    pass
  
  def promote(self):
    pass


"""---------------------------------------------TEST------------------------------------------"""
# p1 = Piece(Pawn(0), 6, 4, 0)
# p2 = Piece(Pawn(0, True), 5, 5, 0)

# pieces = [p1, p2]

# p3 = Piece(Pawn(1), 5, 4, 1)
# valid_squares = p3.piece_type.calc_valid_squares(p3.col, p3.row, pieces)
# print(valid_squares)
