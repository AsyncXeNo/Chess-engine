from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook
from .piece import Piece

def fen_decrypter(fen_string):
  fen = fen_string.split(' ')[0]
  pieces = []

  piece_type_from_symbol = {
    'p' : Pawn,
    'k' : King,
    'n' : Knight,
    'b' : Bishop,
    'q' : Queen,
    'r' : Rook
  }

  row, col = 8, 0

  for letter in fen:
    if letter == '/':
      col = 0
      row -= 1
    else:
      if letter.isnumeric():
        col += int(letter)
      else:
        piece_color = 1 if letter.isupper() else 0
        letter = letter.lower()
        piece_type = piece_type_from_symbol[letter](piece_color)
        col += 1
        pieces.append(Piece(piece_type, row, col, piece_color))

  return pieces
