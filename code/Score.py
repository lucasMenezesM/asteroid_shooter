import pygame
from settings import *

class Score:
  def __init__(self):
    self.font = pygame.font.Font("./graphics/subatomic.ttf", 50)
    

  def update(self, surface):
    score = pygame.time.get_ticks() // 1000
    score_text = f"Score: {score}"
    text_surf = self.font.render(score_text, True, "white")
    text_rect = text_surf.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 90))
    surface.blit(text_surf, text_rect)
    pygame.draw.rect(surface, "white", text_rect.inflate(30,30), width=8, border_radius=5)