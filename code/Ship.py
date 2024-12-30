import pygame
from settings import *
from Laser import Laser
import sys


class Ship(pygame.sprite.Sprite):
  def __init__(self, group):
    super().__init__(group)
    self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
    self.rect = self.image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-80))
    self.mask = pygame.mask.from_surface(self.image)

    self.cooldown_shoot = 500
    self.can_shoot = True
    self.shoot_time = None
    self.font = pygame.font.Font("./graphics/subatomic.ttf", 20)

    self.lives = 3


  def input_position(self):
    pos = pygame.mouse.get_pos()
    self.rect.center = pos


  def laser_timer(self):
    if not self.can_shoot:
      current_time = pygame.time.get_ticks()
      if current_time - self.shoot_time > self.cooldown_shoot:
        self.can_shoot = True
      

  def laser_shoot(self, laser_group):
    self.laser_timer()
    if pygame.mouse.get_pressed()[0] and self.can_shoot:
      self.shoot_time = pygame.time.get_ticks()
      self.can_shoot = False

      # creating a new laser
      Laser(laser_group, self.rect.midtop)


  def meteor_collision(self, meteor_group: pygame.sprite.Group):
    if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
      self.lives -=1
      print(self.lives)


  def display_lives(self, surface: pygame.surface.Surface):
    text = f"Lives: {self.lives}"
    text_surf = self.font.render(text, True, "white")
    text_rect = text_surf.get_rect(midleft=(30, WINDOW_HEIGHT - 30))
    surface.blit(text_surf, text_rect)


  def update(self, surface, laser_group, meteor_group: pygame.sprite.Group):
    self.input_position()
    self.laser_shoot(laser_group)
    self.meteor_collision(meteor_group=meteor_group)
    self.display_lives(surface)