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
        self.__cards = []
        self.shuffle()

    def shuffle(self):
        """Put all the used cards back into the deck,
        and shuffle it into a random order.
        """
        self.__cards.clear()
        try:
            for suit, rank in itertools.product(
                    Card.get_suits(no_jokers=True),
                    Card.get_ranks(no_jokers=True)):
                self.__cards.append(Card(suit=suit, rank=rank))
            if self.joker_support and Card.support_joker:
                for val in Card.get_jocker_values():
                    self.__cards.append(Card(suit="Joker", rank=val))
        except Exception:
            raise Exception("Cannot generate the deck")
        random.shuffle(self.__cards)

    def remaining(self):
        """As cards are dealt from the deck, the number of cards remaining decreases.
        This function returns the number of cards remaining in the deck.
        """
        return len(self.__cards)

    def deal(self):
        """Deals one card from the deck and returns it. If no more cards are left,
           an exception is thrown.
        """
        try:
            return self.__cards.pop()
        except IndexError:
            # Comment: we can raise other exception if needed
            raise IndexError("No more cards left")
