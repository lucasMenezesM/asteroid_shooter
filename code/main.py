import pygame, sys
from settings import *

# Basic Setup
pygame.init()
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Arena Shooter")

# game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  dt = clock.tick(120) / 1000

  pygame.display.update()
  