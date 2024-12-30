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

game_state = "start"

def game_over():
  game_state = "gameover"
  while True:
    display_surface.fill("black")
    font = pygame.font.Font("./graphics/subatomic.ttf", 70)
    text = f"Game Over"
    text_surf = font.render(text, True, "white")
    text_rect = text_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    display_surface.blit(text_surf, text_rect)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_state = "start"
      
    if game_state == "start":
      return "start"
      
    pygame.display.update()


# game loop

def start_game():
  while True:
    # draw background
    display_surface.blit(background_surf, (0,0))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == meteor_event:
        Meteor(meteor_group)

    dt = clock.tick(120) / 1000

    # graphics
    spaceship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)

    # score display
    score.update(surface=display_surface)

    # updates
    if ship.lives == 0:
      return "gameover"

    spaceship_group.update(display_surface, laser_group, meteor_group)
    laser_group.update(dt=dt, meteor_group=meteor_group)
    meteor_group.update(dt)

    pygame.display.update()
  
while True:
  if game_state == "start":
    game_state = start_game()
  elif game_state == "gameover":
    game_state = game_over()