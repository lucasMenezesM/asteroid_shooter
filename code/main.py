import pygame, sys
from settings import *
from Ship import Ship

# Basic Setup
pygame.init()
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Arena Shooter")

# background
background_surf = pygame.image.load("./graphics/background.png").convert()

# sprite groups
spaceship_group = pygame.sprite.GroupSingle()
laser_group = pygame.sprite.Group()

# ship
ship = Ship(spaceship_group)

# get mouse invisible
pygame.mouse.set_visible(False)

# game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  dt = clock.tick(120) / 1000

  # draw background
  display_surface.blit(background_surf, (0,0))

  # graphics
  spaceship_group.draw(display_surface)
  laser_group.draw(display_surface)

  # updates
  spaceship_group.update(laser_group)
  laser_group.update(dt)

  pygame.display.update()
  