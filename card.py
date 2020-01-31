class Card:
    """
    Has two attributes, the value and rank
    There are 4 supported suits - spades, hearts, diamonds, clubs.
    Each of the following suits (spade, heart, diamond, and club)
    Has one of 13 possible ranks:
    ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, or king.
    Ranks are not duplicated within a suit.
    The 'special' suit Joker does not need to be supported,
    but there may be a future requirement to include it.
    """

    # Order of suits are alphabetical based,
    # e.g. lowest is clubs and highest is spades.

    # Comment: I assumed Joker has the highest value
    # Comment: I've decided to go with int values instead of doing
    # a separate class
    __suits = {"Clubs": 1, "Diamonds": 2, "Hearts": 3, "Spades": 4, "Joker": 5}

    # Aces are considered to have the lowest rank.

    # Comment: I assumed we have Joker of 2 colors and
    # they have the highest value
    __joker_values = {"Black": 14, "Red": 14}
    __regular_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                        "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11,
                        "Queen": 12, "King": 13}
    __values = {**__regular_values, **__joker_values}

    support_joker = False

    @classmethod
    def get_ranks(cls, no_jokers=False):
        if cls.support_joker and not no_jokers:
            return cls.__values.keys()
        else:
            return cls.__regular_values.keys()

    @classmethod
    def get_suits(cls, no_jokers=False):
        if cls.support_joker and not no_jokers:
            return cls.__suits.keys()
        else:
            return [val for val in cls.__suits.keys()
                    if val != "Joker"]

    @classmethod
    def get_jocker_values(cls):
        return cls.__joker_values.keys()

    def __init__(self, suit, rank):
        """Constructor for Card"""
        if suit not in self.get_suits():
            raise Exception(
                "Wrong suit {suit}. We support only {suits}".format(
                    suit=suit, suits=self.get_suits()))

        if self.support_joker and suit == "Joker"\
                and rank not in self.get_ranks():
            raise Exception("Joker card must have {jocker_ranks} ranks, "
                            "not {rank}.".format(jocker_ranks=self.get_ranks(),
                                                 rank=rank))

        if rank not in self.get_ranks():
            raise Exception(
                "Wrong rank {rank}. We support only {ranks}".format(
                    rank=rank, ranks=self.get_ranks()))

        self.__rank = rank
        self.__suit = suit

    def suit(self):
        """Returns int value of the suit of this card"""
        return self.__suits[self.__suit]

    def value(self):
        """Returns the value, which is one of the numbers
        1 through 13, inclusive for a regular card
        """
        return self.__values[self.__rank]

    def suitAsString(self):
        """Returns a String representation of the card's suit.
        ("Spades", "Clubs")
        """
        return self.__suit

    def valueAsString(self):
        """Returns a String representation of the card's value
        (e.g. "Ace", "2")
        """
        return self.__rank

    def __str__(self):
        """Returns a string representation of this card, including both its
        suit and its value. (e.g. "Queen of Hearts", "10 of Diamonds")
        """
        return "{rank} of {suit}".format(rank=self.valueAsString(),
                                         suit=self.suitAsString())

    # Comment: __str__ is better, but I kept this as well
    def toString(self):
        """Returns a string representation of this card, including both its
           suit and its value. (e.g. "Queen of Hearts", "10 of Diamonds")
        """
        return self.__str__()

    # Comment: I've decided to implement comparison by value (see sortByValue)
    # by default for card class
    def __lt__(self, other):
        return ((self.value(), self.suit()) < (other.value(), other.suit()))

    def __gt__(self, other):
        return ((self.value(), self.suit()) > (other.value(), other.suit()))

    def __eq__(self, other):
        return ((self.value(), self.suit()) == (other.value(), other.suit()))
