import pygame
from chess.constants import WIDTH, HEIGHT
from chess.board import Board 

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def main():
  run = True
  clock = pygame.time.Clock()
  board = Board()

  while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        pass

    board.draw(WIN)
    pygame.display.update()

  pygame.quit()


print(__file__)
main()
