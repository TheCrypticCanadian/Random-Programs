import random as random
# A basic data structure for a deck object 

class Deck:

    def __init__(self):
        self.cards = []
        self.discard = []

    def discard(self,card):
        self.discard.append(card)
    
    def draw_card(self):
        card = self.cards.pop()
        print(len(self.cards))
        return card

    def init_deck(self):
        suits = ["Spades","Hearts","Clubs","Diamonds"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in suits:
            for value in values:
                card = Card(suit,value)
                self.cards.append(card)
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

