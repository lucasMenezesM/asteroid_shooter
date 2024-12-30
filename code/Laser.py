from settings import *
import pygame

class Laser(pygame.sprite.Sprite):
  def __init__(self, groups, pos: tuple[int, int]):
    super().__init__(groups)
    self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
    self.rect = self.image.get_rect(midbottom=pos)
    self.mask = pygame.mask.from_surface(self.image)
 
    self.pos = pygame.math.Vector2(self.rect.topleft)
    self.direction = pygame.math.Vector2(0, -1)
    self.speed = 600

    self.explosion_sound = pygame.mixer.Sound("./sounds/explosion.wav")

  def meteor_collision(self, meteor_group: pygame.sprite.Group):
    if pygame.sprite.spritecollide(self, meteor_group,True):
      self.kill()
      self.explosion_sound.play()

  def update(self, meteor_group: pygame.sprite.Group, dt):
    self.pos += self.direction * self.speed * dt
    self.rect.topleft = (round(self.pos.x), round(self.pos.y))
    self.meteor_collision(meteor_group=meteor_group)

    if self.rect.bottom < 0:
      self.kill()