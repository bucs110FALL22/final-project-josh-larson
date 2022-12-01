import pygame
import random
from src.deck import Deck

class Controller(pygame.sprite.Sprite):
    def __init__(self):
      #setup pygame data
      def __init__(self, deck = None, card = None, suite = None):
        super().__init__()
        pygame.init()
        pygame.init()
        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.images = ["../assets/background.jpeg"]
        self.background = pygame.image.load(self.images[0])
        self.background = pygame.transform.scale(self.background, size)
        pygame.display.set_caption('Blackjack')
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        pygame.display.flip()
        self.deck = []
        self.card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suite = ["Spade", "Heart", "Diamond", "Club"]
        for s in self.suite:
          for c in self.card:
            self.deck.append((s, c)) 
        print(deck)
      #, self.card_sprite(s,c)))
      def value(self, card):
        card = card[1]
        if card in ("A"):
          num = int(input("Enter: Would you like this Ace to be worth 1 or 11?"))
          return int(num)
        elif card in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
          value = int(card)
          return value
        elif card in ("J", "Q", "K"):
          value = int(10)
          return value

    def mainloop(self):   #deal
      self.player_hand = []
      self.player_sum = 0 
      self.dealer_hand = []
      self.dealer_sum = 0
      
      while len(self.dealer_hand) < 2:
        for i in range(2): 
          player_selected_card = random.choice(self.deck)
          self.player_hand.append(player_selected_card)
          self.deck.remove(player_selected_card)
          #return player_selected_card
        for card in self.player_hand:
          self.player_sum += self.value(card)   
        print("Player has: ", self.player_hand, "Their total score is: ", self.player_sum)
  
        for i in range(2):
          dealer_selected_card = random.choice(self.deck)
          self.dealer_hand.append(dealer_selected_card)
          self.deck.remove(dealer_selected_card)
        for card in self.dealer_hand:
          self.dealer_sum += self.value(card)
        print("Dealer has: ", self.dealer_hand, "Their total score is: ", self.dealer_sum)
      self.hit()
        
      return self.player_hand










    
  