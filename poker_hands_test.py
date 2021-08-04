import pytest
from poker_hands import check_hand

def test_raise_exception_if_hand_is_empty():
    with pytest.raises(Exception):
        check_hand("")

def test_straight_flush_wins():
    test_hand = "Black: 2H 3D 5S 9C KD  White: 2H 3H 4H 5H 6H"
    assert check_hand(test_hand) == "White wins, - with Straight Flush"