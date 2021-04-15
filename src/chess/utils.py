from .pieces.bishop import Bishop
from .pieces.king import King
from .pieces.knight import Knight
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook
from .piece import Piece

def fen_decrypter(fen_string):
  fen1 = fen_string.split(' ')[0]
  fen2 = fen_string.split(' ')[1]
  fen3 = fen_string.split(' ')[2]
  fen4 = fen_string.split(' ')[3]
  fen5 = fen_string.split(' ')[4]
  fen6 = fen_string.split(' ')[5]

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

  num_of_moves = int(fen6)
  fify_move = int(fen5)
  
  if fen4 != '-':
    en_passant_square = (ord(fen4[0]) -96, int(fen4[1]),)
  
  else:
    en_passant_square = None

  wkc = False
  wqc = False
  bkc = False
  bqc = False

  for letter in fen3:
    if letter == 'K':
      wkc = True
    if letter == 'Q':
      wqc = True
    if letter == 'k':
      bkc = True
    if letter == 'q':
      bqc = True

  color_to_move = 1 if fen2 == 'w' else 0

  for letter in fen1:
    if letter == '/':
      col = 0
      row -= 1
    else:
      if letter.isnumeric():
        col += int(letter)
      else:
        piece_color = 1 if letter.isupper() else 0


        if en_passant_square: 
          if letter == 'P':
            if col == en_passant_square[0]:
              if row == en_passant_square[1] + 1:
                piece_type = piece_type_from_symbol[letter.lower()](piece_color, can_be_en_passant=True)
          if letter == 'p':
            if col == en_passant_square[0]:
              if row == en_passant_square[1] - 1:
                piece_type = piece_type_from_symbol[letter.lower()](piece_color, can_be_en_passant=True)


        if not wkc:
          if letter == 'K':
            piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
          if letter == 'R':
            if row == 1 and col == 8:
              piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
        
        if not wqc:
          if letter == 'K':
            piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
          if letter == 'R':
            if row == 1 and col == 1:
              piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)

        if not bkc:
          if letter == 'k':
            piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
          if letter == 'r':
            if row == 8 and col == 8:
              piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
        
        if not wqc:
          if letter == 'k':
            piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)
          if letter == 'r':
            if row == 8 and col == 1:
              piece_type = piece_type_from_symbol[letter.lower()](piece_color, first_move=False)


        else:
          piece_type = piece_type_from_symbol[letter.lower()](piece_color)

        col += 1
        pieces.append(Piece(piece_type, row, col, piece_color))

  return pieces, color_to_move, num_of_moves
