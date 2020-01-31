import card
import deck
import hand
import pytest

# card tests


def test_create_card():
    card1 = card.Card("Spades", "Ace")
    assert card1.value() == 1
    assert card1.suit() == 4
    assert card1.suitAsString() == "Spades"
    assert card1.valueAsString() == "Ace"


@pytest.mark.xfail
def test_create_card_wrong_suit():
    card1 = card.Card("Spad", "2")


@pytest.mark.xfail
def test_create_card_wrong_rank():
    card1 = card.Card("Spade", "aa")


def test_get_ranks():
    assert ["Ace", "2", "3", "4", "5", "6", "7", "8",
            "9", "10", "Jack", "Queen", "King"] == [*card.Card.get_ranks()]


def test_get_suits():
    assert \
        ["Clubs", "Diamonds", "Hearts", "Spades"] == [*card.Card.get_suits()]


def test_get_ranks_w_joker():
    card.Card.support_joker = True
    assert ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack",
            "Queen", "King", "Black", "Red"] == [*card.Card.get_ranks()]


def test_get_suits_w_joker():
    card.Card.support_joker = True
    assert ["Clubs", "Diamonds", "Hearts", "Spades",
            "Joker"] == [*card.Card.get_suits()]


def test_joker_values():
    card.Card.support_joker = True
    assert ["Black", "Red"] == [*card.Card.get_jocker_values()]


def test_joker_card():
    card.Card.support_joker = True
    card1 = card.Card("Joker", "Black")
    assert card1.value() == 14
    assert card1.suit() == 5
    assert card1.suitAsString() == "Joker"
    assert card1.valueAsString() == "Black"


@pytest.mark.xfail
def test_joker_card_wrong():
    card.Card.support_joker = True
    card1 = card.Card("Joker", "ddd")


@pytest.mark.xfail
def test_joker_card_no_support():
    card1 = card.Card("Joker", "Black")


def test_get_suits_no_joker():
    card.Card.support_joker = True
    assert ["Clubs", "Diamonds", "Hearts",
            "Spades"] == [*card.Card.get_suits(no_jokers=True)]


def test_ranks_no_jocker():
    card.Card.support_joker = True
    assert ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
            "Jack", "Queen", "King"] == [*card.Card.get_ranks(no_jokers=True)]


# deck tests


def test_deck():
    deck1 = deck.Deck()
    assert deck1.remaining() == 52
    card1 = deck1.deal()
    print(card1)
    assert deck1.remaining() == 51
    deck1.shuffle()
    assert deck1.remaining() == 52


@pytest.mark.xfail
def test_deck_deal53():
    deck1 = deck.Deck()
    for i in range(0, 55):
        card1 = deck1.deal()


def test_deck_w_joker():
    deck.Deck.joker_support = True
    deck1 = deck.Deck()
    assert deck1.remaining() == 54


# hand tests


def test_check_sortBySuit():
    hand1 = hand.Hand()
    hand1.addCard(card.Card("Spades", "2"))
    hand1.addCard(card.Card("Spades", "3"))
    hand1.addCard(card.Card("Clubs", "3"))
    hand1.addCard(card.Card("Spades", "Ace"))
    hand1.addCard(card.Card("Hearts", "Ace"))
    hand1.addCard(card.Card("Diamonds", "3"))
    hand1.addCard(card.Card("Spades", "5"))
    hand1.addCard(card.Card("Hearts", "King"))
    hand1.addCard(card.Card("Hearts", "3"))
    hand1.sortBySuit()
    assert str(hand1) == "3 of Clubs, 3 of Diamonds, Ace of Hearts, "\
                         "3 of Hearts, King of Hearts, Ace of Spades, " \
                         "2 of Spades, 3 of Spades, 5 of Spades"


def test_check_sortByValue():
    hand1 = hand.Hand()
    hand1.addCard(card.Card("Spades", "2"))
    hand1.addCard(card.Card("Spades", "3"))
    hand1.addCard(card.Card("Spades", "Ace"))
    hand1.addCard(card.Card("Hearts", "Ace"))
    hand1.addCard(card.Card("Hearts", "King"))
    hand1.addCard(card.Card("Spades", "5"))
    hand1.addCard(card.Card("Hearts", "3"))
    hand1.addCard(card.Card("Diamonds", "3"))
    hand1.addCard(card.Card("Clubs", "3"))
    hand1.sortByValue()
    assert str(hand1) == "Ace of Hearts, Ace of Spades, 2 of Spades, "\
                         "3 of Clubs, 3 of Diamonds, 3 of Hearts, "\
                         "3 of Spades, 5 of Spades, King of Hearts"


def test_hand_add_remove_card_hand():
    hand1 = hand.Hand()
    hand1.addCard(card.Card("Spades", "2"))
    assert str(hand1) == "2 of Spades"
    card2 = card.Card("Spades", "3")
    hand1.addCard(card2)
    assert str(hand1) == "2 of Spades, 3 of Spades"
    hand1.removeCard(card2)
    assert str(hand1) == "2 of Spades"


def test_add_card_from_deck():
    hand1 = hand.Hand()
    deck1 = deck.Deck()
    assert str(hand1) == ""
    hand1.addCard(deck1.deal())
    assert str(hand1) != ""
