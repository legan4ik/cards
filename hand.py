class Hand:
    """A set of cards, which have been dealt from a Deck.
    The number of cards in a hand is only restricted by the number
    of cards contained in a Deck (e.g. 0 to 52)
    """

    def __init__(self):
        self.__cards = []

    def addCard(self, card):
        """Add a Card to the hand"""
        self.__cards.append(card)

    def removeCard(self, card):
        """Removes a Card from the hand"""
        self.__cards.remove(card)

    def sortBySuit(self):
        """Sorts the cards in the hand so that cards other same suit
        are grouped together, and within a suit the cards are sorted by rank.
        """
        # the other way how we can sort
        self.__cards.sort(key=lambda card: (card.suit(), card.value()))

    def sortByValue(self):
        """Sorts the cards in the hand so that cards are sorted into
        order of increasing rank. Cards with the same rank are sorted by suit.
        """
        self.__cards.sort()

    def __str__(self):
        text = ""
        for card in self.__cards:
            text += card.toString() + ", "
        return text.strip(", ")
