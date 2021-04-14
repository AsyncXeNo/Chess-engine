import pygame
from .constants import SQUARE_SIZE

class Piece:
  def __init__(self, piece_type, row, col, color):
    self.row = row
    self.col = col
    self.color = color
    self.piece_type = piece_type

    self.x = 0
    self.y = 0
    self.calc_pos()

  def __str__(self):
    return f'type: {self.piece_type.__str__()} color: {self.color} pos: <{self.col}, {self.row}>'

  def calc_pos(self):
    self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
    self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

  def draw(self, win):
    self.piece_type.draw(self.color)
