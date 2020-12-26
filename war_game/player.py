class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def single(self):
        return self.cards.pop(0)

    def war(self, quantity=1):
        dealt = []
        for i in range(quantity):
            dealt.append(self.cards.pop(0))
        return dealt

    def win_turn(self, new_cards):
        self.cards = new_cards + self.cards
        return self

    def cards_count(self):
        return len(self.cards)

    def __str__(self):
        return f'Player {self.name}: {self.cards_count()} cards'
