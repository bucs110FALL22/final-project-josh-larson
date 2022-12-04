import pygame
import random
from src.deck import Deck

class Controller(pygame.sprite.Sprite):

    def __init__(self, deck=None, card=None, suite=None, hit=None):
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode()
        size = pygame.display.get_window_size()
        self.images = ["assets/background.jpeg"]
        self.background = pygame.image.load(self.images[0])
        self.background = pygame.transform.scale(self.background, size)
        pygame.display.set_caption('Blackjack')
        self.screen.blit(self.background, (0, 0))
        width = 370
        height = 266
        red = [200, 0, 0]
        blue = [0, 0, 200]
        hit_text_cor = (100, 190)
        stand_text_cor = (370, 190)
        hitbox_width = width / 4
        hitbox_height = height / 4
        hitbox_width = int(hitbox_width)
        hitbox_height = int(hitbox_height)
        pygame.draw.rect(self.screen, red, [360, 190, 80, 30])
        pygame.draw.rect(self.screen, blue, [80, 190, 80, 30])
        pygame.display.update()
        pygame.display.flip()
        self.font = pygame.font.SysFont('Arial', 25)
        self.screen.blit(self.font.render('HIT', True, (255, 255, 255)),hit_text_cor)
        self.screen.blit(self.font.render('STAY', True, (255, 255, 255)),stand_text_cor)
        pygame.display.update()
        pygame.display.flip()
        self.deck = []
        self.card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.suite = ["Spade", "Heart", "Diamond", "Club"]
        for s in self.suite:
            for c in self.card:
                self.deck.append((s, c))
        print(deck)

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

    def hit(self):
      mouse = pygame.mouse.get_pos()
      hit_results = []
      player_hit = input("Would you like to hit? Enter 1 (click blue) for Yes or 2 (click red) for No.")
      if player_hit == "1":
        if pygame.MOUSEBUTTONDOWN:
          if 80 <= mouse[0] <= 160 and 190 <= mouse[1] <= 220:
            print("You chose to hit")
            player_hit_card = random.choice(self.deck)
            self.player_hand.append(player_hit_card)
            self.deck.remove(player_hit_card)
            self.player_sum += self.value(player_hit_card)
            print("Player's new card is ", player_hit_card)
            print("Player has: ", self.player_hand, "Their total score is: ", self.player_sum)
      if player_hit == "2":
        if 360 <= mouse[0] <= 440 and 190 <= mouse[1] <= 220:
          print("You chose to stay")
          print("Player has: ", self.player_hand, "Their total score is: ", self.player_sum)
      return hit_results
    
    def mainloop(self):  
        self.player_hand = []
        self.player_sum = 0
        self.dealer_hand = []
        self.dealer_sum = 0

        while len(self.dealer_hand) < 2:
            for i in range(2):
                player_selected_card = random.choice(self.deck)
                self.player_hand.append(player_selected_card)
                self.deck.remove(player_selected_card)
            for card in self.player_hand:
                self.player_sum += self.value(card)
            print("Player has: ", self.player_hand, "Their total score is: ",
                  self.player_sum)

            for i in range(2):
                dealer_selected_card = random.choice(self.deck)
                self.dealer_hand.append(dealer_selected_card)
                self.deck.remove(dealer_selected_card)
            for card in self.dealer_hand:
                self.dealer_sum += self.value(card)
            print("Dealer has: ", self.dealer_hand, "Their total score is: ",
                  self.dealer_sum)
            self.hit()
            return self.player_hand

    def winner(self):
        if self.player_sum == 21:
            print("You won! Blackjack!")
            pygame.display.set_caption('You Won Blackjack')
        if self.player_sum > 21:
            print("You lost! You busted!")
            pygame.display.set_caption('You Lost Blackjack')
        if self.dealer_sum == 21 and self.player_sum == 21:
            print("It's a tie!")
            pygame.display.set_caption('It is a tie!')
        if self.player_sum > self.dealer_sum:
            if self.player_sum > 21:
                print("")
            elif self.player_sum < 21:
                print("You won! You had a higher score than the dealer!")
                pygame.display.set_caption('You Won Blackjack')
        if self.player_sum < self.dealer_sum:
            if self.dealer_sum > 21:
                print("")
            elif self.dealer_sum < 21:
                print("You lost! The dealer had a higher score than you!")
                pygame.display.set_caption('You Lost Blackjack')

    def card_sprite(self, suite, card):
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
            elif card in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
                card = card
            x = 10
            y = 10
            card_name = f"{card}_of_{suite.lower()}s.svg"
            card_image = f"assets/card_images/{card_name}"
            img = pygame.image.load(card_image)
            pygame.transform.scale(self.screen, (x, y))
            self.screen.blit(img, (150, 0))
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
    deck.card_sprite("Heart", "A")


def main():
    deck = Controller()
    deck.self.mainloop


main()










    
  