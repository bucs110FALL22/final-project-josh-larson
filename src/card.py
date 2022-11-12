import pygame

class Card(pygame.sprite.Sprite):
  def __init__(self, value, x, y):
    super().__init__(self)
    self.value = value
    self.x = x
    self.y = y
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

    def move_up(self):
      self.rect.y += self.move
      self.rect.y -= self.move
      self.rect.x += self.speed
      self.rect.x -= self.speed
  