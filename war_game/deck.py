from war_game.card import Card
from random import shuffle
import math

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')


class Deck:
    def __init__(self):
        self.deck = []

        for rank in ranks:
            for suit in suits:
                self.deck.append(Card(suit, rank))

    def deal(self, quantity=1):
        dealt = []
        for i in range(quantity):
            dealt.append(self.deck.pop())
        return dealt

    def shuffle(self):
        shuffle(self.deck)
        return self

    def add_cards(self, cards):
        self.deck = self.deck + cards
        return self

    def deck_split(self):
        for d in self.deck:
            print(d)
        half = int(math.ceil(len(self.deck) / 2))
        return self.deal(half)
