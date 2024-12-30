import pygame, sys
from settings import *
from Ship import Ship
from Meteor import Meteor
from Score import Score

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
meteor_group = pygame.sprite.Group()

# Score
score = Score()

# ship
ship = Ship(spaceship_group)

# get mouse invisible
pygame.mouse.set_visible(False)

# meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

# game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    if event.type == meteor_event:
      print("meteor created")
      Meteor(meteor_group)

  dt = clock.tick(120) / 1000

  # draw background
  display_surface.blit(background_surf, (0,0))

  # graphics
  spaceship_group.draw(display_surface)
  laser_group.draw(display_surface)
  meteor_group.draw(display_surface)

  # score display
  score.update(surface=display_surface)

  # updates

  if ship.lives == 0:
    pygame.quit()
    sys.exit()
    
  spaceship_group.update(display_surface, laser_group, meteor_group)
  laser_group.update(dt)
  meteor_group.update(dt)


  pygame.display.update()
  