"""
Implement a Deck of Cards, which can be used to fill Hands of Cards
"""

import card
import deck
import hand

# creating card
card1 = card.Card("Spades", '2')

# init deck
deck1 = deck.Deck()
print (deck1.remaining())
for i in deck1.cards:
    print(i)

# init hand
hand1 = hand.Hand()
hand1.addCard(card1)
hand1.sortByValue()
print(hand1)

