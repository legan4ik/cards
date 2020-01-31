from card import Card
import itertools
import random


class Deck:
    """
    Composed of 52 cards, no duplicates
    Once a card has been dealt from a deck, it cannot be dealt
    again until the deck has been shuffled.
    """

    joker_support = False

    def __init__(self):
        self.cards = []
        self.shuffle()

    def shuffle(self):
        """Put all the used cards back into the deck,
        and shuffle it into a random order.
        """
        self.cards.clear()
        for suit, rank in itertools.product(Card.get_suits(no_jokers=True),
                                            Card.get_ranks(no_jokers=True)):
            self.cards.append(Card(suit=suit, rank=rank))
        if self.joker_support and Card.support_joker:
            for val in Card.get_jocker_values():
                self.cards.append(Card(suit="Joker", rank=val))
        random.shuffle(self.cards)

    def remaining(self):
        """As cards are dealt from the deck, the number of cards remaining decreases.
        This function returns the number of cards remaining in the deck.
        """
        return len(self.cards)

    def deal(self):
        """Deals one card from the deck and returns it. If no more cards are left,
           an exception is thrown.
        """
        try:
            return self.cards.pop()
        except IndexError:
            print("No more cards left")
            # Comment: we can raise other exception if needed
            raise IndexError
