import pygame
from settings import *
from Laser import Laser

class Ship(pygame.sprite.Sprite):
  def __init__(self, group):
    super().__init__(group)
    self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
    self.rect = self.image.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-80))

    self.cooldown_shoot = 500
    self.can_shoot = True
    self.shoot_time = None


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


  def update(self, laser_group):
    self.input_position()
    self.laser_shoot(laser_group)