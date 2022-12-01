import pygame
import random 


class Deck(pygame.sprite.Sprite):
  def __init__(self, deck = None, card = None, suite = None):
    super().__init__()
    pygame.init()
    self.screen = pygame.display.set_mode()
    size = pygame.display.get_window_size()
    #print(size)
    self.images = ["../assets/background.jpeg"]
    self.background = pygame.image.load(self.images[0])
    self.background = pygame.transform.scale(self.background, size)
    pygame.display.set_caption('Blackjack')
    self.screen.blit(self.background, (0,0))
    width = 370
    height = 266
    red = [200, 0, 0]
    blue = [0, 0, 200]
    hitbox_width = width / 4
    hitbox_height = height / 4
    red_button = pygame.Rect(0, 0, hitbox_width, hitbox_height)
    blue_button = pygame.Rect(0, 0, hitbox_width, hitbox_height)
    blue_button.topleft = red_button.topright
    red_button = pygame.draw.rect(self.screen, red, red_button)
    blue_button = pygame.draw.rect(self.screen, blue, blue_button)
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
      num = int(1) #input("Enter: Would you like this Ace to be worth 1 or 11?"))
      return int(num)
    elif card in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
      value = int(card)
      return value
    elif card in ("J", "Q", "K"):
      value = int(10)
      return value
  
  def mainloop(self): #deal
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
      

  def hit(self): #hit in controller #add self.hit
    hit_results = []
    player_hit = input("Would you like to hit? Enter 1 for Yes or 2 for No.")
    if player_hit == "1":
      print("You chose to hit")
      player_hit_card = random.choice(self.deck)
      self.player_hand.append(player_hit_card)
      self.deck.remove(player_hit_card)
      self.player_sum += self.value(player_hit_card)
      print("Player's new card is ", player_hit_card) #append to hit results if they choose to hit
      print("Player has: ", self.player_hand, "Their total score is: ", self.player_sum) #return this string
    if player_hit == "2":
      print("You chose to stay")
      print("Player has: ", self.player_hand, "Their total score is: ", self.player_sum) #append to hit results if they choose to stay
    return hit_results


  def winner(self): #return a string
    if self.player_sum == 21:
      print("You won! Blackjack!") 
    if self.player_sum > 21:
      print("You lost! You busted!")
    if self.dealer_sum == 21 and self.player_sum == 21:
      print("It's a tie!")
    if self.player_sum > self.dealer_sum:
      if self.player_sum > 21:
        print("")
      elif self.player_sum < 21:
        print("You won! You had a higher score than the dealer!")
    if self.player_sum < self.dealer_sum:
      if self.dealer_sum > 21:
        print("")
      elif self.dealer_sum < 21:
        print("You lost! The dealer had a higher score than you!")

  def card_sprite(self,suite,card):
      while True:
        if not card.isnumeric():
          if card == "A":
            card = "ace"
          if card == "J":
            card = "jack"
          if card == "Q":
            card = "queen"
          if card == "K":
            card = "king"
        elif card in ("2", "3", "4", "5", "6", "7", "8", "9","10"):
          card = card
        x = 10
        y = 10
        card_name = f"{card}_of_{suite.lower()}s.svg"
        card_image = f"../assets/card_images/{card_name}"
        img = pygame.image.load(card_image)
        pygame.transform.scale(self.screen, (x,y)) #use constants for card sizes instead of magic values
        self.screen.blit(img, (150,50))
        pygame.display.update()
        return card_image

        
  def gameTest(self):
    self.mainloop()
    while self.hit() == 2:
      continue
    self.winner()

deck = Deck()
deck.gameTest()
while True:
  deck.card_sprite("Heart","A")
  
      
    