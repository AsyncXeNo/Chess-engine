import pygame
import os
from .constants import SQUARE_SIZE

dir_path = os.path.dirname(os.path.realpath(__file__))

pieces = {
  1: {
    'p': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/pawn.png'), (64, 64)),
    'b': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/bishop.png'), (64, 64)),
    'k': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/king.png'), (64, 64)),
    'n': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/knight.png'), (64, 64)),
    'q': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/queen.png'), (64, 64)),
    'r': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/white/rook.png'), (64, 64)),
  },
  0: {
    'p': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/pawn.png'), (64, 64)),
    'b': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/bishop.png'), (64, 64)),
    'k': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/king.png'), (64, 64)),
    'n': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/knight.png'), (64, 64)),
    'q': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/queen.png'), (64, 64)),
    'r': pygame.transform.scale(pygame.image.load(f'{dir_path}/../assets/black/rook.png'), (64, 64)),
  }
}

class Piece:
  def __init__(self, piece_type, row, col, color):
    print(dir_path)
    self.row = row
    self.col = col
    self.color = color
    self.piece_type = piece_type

    self.image = pieces[self.color][self.piece_type.__str__()[0].lower()]
    self.image_rect = self.image.get_rect()

    self.calc_pos()

  def __str__(self):
    return f'type: {self.piece_type.__str__()} color: {self.color} pos: <{self.col}, {self.row}>'

  def calc_pos(self):
    print(SQUARE_SIZE)
    self.image_rect.center = (SQUARE_SIZE * self.col) - (SQUARE_SIZE // 2), (SQUARE_SIZE * (9 - self.row)) - (SQUARE_SIZE // 2)

  def draw(self, win):
    win.blit(self.image, self.image_rect)
