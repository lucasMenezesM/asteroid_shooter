import pygame
from random import randint, uniform, choice
from settings import *

meteors_size = [(90,90), (110, 110), (130, 130), (150,150),(180,180)]

class Meteor(pygame.sprite.Sprite):
  def __init__(self, groups):
    super().__init__(groups)

    meteor_surf = pygame.image.load("./graphics/meteor.png").convert_alpha()

    self.scaled_surf = pygame.transform.scale(meteor_surf, choice(meteors_size))
    self.image = self.scaled_surf
    self.rect = self.image.get_rect(midbottom=(randint(-100, WINDOW_HEIGHT+100), -10))
    self.mask = pygame.mask.from_surface(self.image)

    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2(uniform(-1,1), 1)
    self.speed = randint(300, 500)
   
    # rotation logic
    self.rotation = 0
    self.rotation_speed = randint(20,50)

  def rotate(self, dt):
    self.rotation += self.rotation_speed * dt
    self.image = pygame.transform.rotozoom(self.scaled_surf, self.rotation, 1)
    self.rect = self.image.get_rect(center=self.rect.center)
    self.mask = pygame.mask.from_surface(self.image)

  def update(self, dt):
    self.pos += self.speed * self.direction * dt
    self.rect.topleft = (round(self.pos.x), round(self.pos.y))
    self.rotate(dt)

    if self.rect.top > WINDOW_HEIGHT:
      self.kill()
