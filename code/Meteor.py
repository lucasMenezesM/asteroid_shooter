import pygame
from random import randint, uniform
from settings import *

class Meteor(pygame.sprite.Sprite):
  def __init__(self, groups):
    super().__init__(groups)

    self.image = pygame.image.load("./graphics/meteor.png").convert_alpha()
    self.rect = self.image.get_rect(midbottom=(randint(-100, WINDOW_HEIGHT+100), -10))

    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2(uniform(-1,1), 1)
    self.speed = 400
   

  def update(self, dt):
    self.pos += self.speed * self.direction * dt
    self.rect.topleft = (round(self.pos.x), round(self.pos.y))
