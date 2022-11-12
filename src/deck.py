import pygame


class Deck(pygame.sprite.Sprite):
  def __init__(self, card, amount, x, y):
    super().__init__(self)
    self.card = card
    self.amount = 52
    self.list = []
    self.x = x
    self.y = y
    self.image = pygame.image.load()
    self.rect = self.image.get_rect()

  def shuffle(self):
    shuffle_deck = sort(self.list)
    return shuffle_deck
      
  def deal(self):
    deal = self.amount - 1
    return deal
  
    