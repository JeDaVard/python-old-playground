from war_game.deck import Deck
from war_game.player import Player

values = {'Two': 0, 'Three': 1, 'Four': 2, 'Five': 3, 'Six': 4, 'Seven': 5, 'Eight': 6, 'Nine': 7, 'Ten': 8, 'Jack': 9,
          'Queen': 10, 'King': 11, 'Ace': 12}

deck = Deck()
deck.shuffle()

# player1_name = input('Player 1, please, your name:\n')
# player2_name = input('Player 2, please, your name:\n')

player1 = Player('Davit', deck.deal(26))
player2 = Player('Selena', deck.deal(26))

table = []
rounds = 0

while player1.cards_count() > 0 and player2.cards_count() > 0:
    print(rounds)
    rounds += 1

    table = table + [player1.single(), player2.single()]

    if values[table[-2].rank] > values[table[-1].rank]:
        player1.win_turn(table)
        table = []
    elif values[table[-2].rank] < values[table[-1].rank]:
        player2.win_turn(table)
        table = []
    else:
        c1 = player1.cards_count()
        c2 = player2.cards_count()

        if c1 == 0 or c2 == 0:
            if all(values[x.rank] == values[table[0].rank] for x in table):
                if c1 > c2:
                    player1.win_turn(table)
                    table = []
                else:
                    player2.win_turn(table)
                    table = []
                break

            deck.add_cards(table).shuffle()
            player1.win_turn(deck.deck_split())
            player2.win_turn(deck.deal(len(deck.deck)))
            table = []
            continue

        if c1 >= 5 and c2 >= 5:
            table = table + player1.war(5) + player2.war(5)
        else:
            break


print(player1)
print(player2)
print("rest", len(table))
print('_________________')
print(f"{player1.name} won!!!" if player1.cards_count() > player2.cards_count() else f"{player2.name} won!!!")
print('_________________')
