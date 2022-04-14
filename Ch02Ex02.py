#!/usr/bin/env python3.7
"""
Mastering Object-Oriented Python 2e

Code Examples for Mastering Object-Oriented Python 2nd Edition

Chapter 2. Example 2.
"""

from typing import Tuple, Any, Union, cast
from enum import Enum

# Definition of a simple class hierarchy.
# Note the overlap with a dataclass if we use properties.


class Card:
    """
    Card object with rank, suit, and _points attributes

    Returns:
        Card object

    Methods for constructor, rank comparison, string representation,
    rank, suit, and relative value of card
    """
    insure = False

    def __init__(self, rank: str, suit: Any) -> None:
        self.suit = suit
        self.rank = rank
        self.hard, self.soft = self._points()

    def __eq__(self, other: Any) -> bool:
        return (
            self.suit == cast("Card", other).suit
            and self.rank == cast("Card", other).rank
            and self.hard == cast("Card", other).hard
            and self.soft == cast("Card", other).soft
        )

    def __repr__(self) -> str:
        """Returns the rank and suit of a given card

        Returns:
            str: rank and suit of card
        """
        return f"{self.__class__.__name__}(suit={self.suit!r}, rank={self.rank!r})"

    def __str__(self) -> str:
        """Returns rank and suit of current card

        Returns:
            str: rank and suit of card
        """
        return f"{self.rank}{self.suit}"

    def _points(self) -> Tuple[int, int]:
        return int(self.rank), int(self.rank)


class AceCard(Card):
    """Ace is a unique card

    Args:
        Card (Card): CARD object of rank 1, any suit

    Returns:
        Bool : used for testing purposes
    """
    insure = True

    def _points(self) -> Tuple[int, int]:
        """returns a tuple representing the point value of a given CARD

        Returns:
            Tuple[int, int]: Use a tuple of 2 ints because Aces may count 1 or 11
            All other cards have a single point value.
        """
        return 1, 11


class FaceCard(Card):
    """Represents K,Q,J rank of CARD

    Args:
        Card (Card): Used to set point values for facecards
    """

    def _points(self) -> Tuple[int, int]:
        return 10, 10


# We can create cards like this

test_card = """
    >>> Suit.Club
    <Suit.Club: '♣'>
    >>> d1 = [AceCard('A', '♠'), Card('2', '♠'), FaceCard('Q', '♠'), ]
    >>> d1
    [AceCard(suit='♠', rank='A'), Card(suit='♠', rank='2'), FaceCard(suit='♠', rank='Q')]
    >>> Card('2', '♠')
    Card(suit='♠', rank='2')
    >>> str(Card('2', '♠'))
    '2♠'
"""

# Instead of strings, we can use an enum


class Suit(str, Enum):
    Club = "♣"
    Diamond = "♦"
    Heart = "♥"
    Spade = "♠"


# We can create cards like this

test_card_suit = """
    >>> cards = [AceCard('A', Suit.Spade), Card('2', Suit.Spade), FaceCard('Q', Suit.Spade),]
    >>> cards
    [AceCard(suit=<Suit.Spade: '♠'>, rank='A'), Card(suit=<Suit.Spade: '♠'>, rank='2'), FaceCard(suit=<Suit.Spade: '♠'>, rank='Q')]
"""

test_suit_value = """
    >>> Suit.Heart.value
    '♥'
    >>> Suit.Heart.value = 'H'  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
      File "/Users/slott/miniconda3/envs/py37/lib/python3.7/doctest.py", line 1329, in __run
        compileflags, 1), test.globs)
      File "<doctest __main__.__test__.test_suit_value[1]>", line 1, in <module>
        Suit.Heart.value = 'H'
      File "/Users/slott/miniconda3/envs/py37/lib/python3.7/types.py", line 175, in __set__
        raise AttributeError("can't set attribute")
    AttributeError: can't set attribute

"""

__test__ = {name: value for name, value in locals().items() if name.startswith("test_")}

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
