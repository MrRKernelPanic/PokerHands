import pytest
from poker_hands import check_hand


def test_raise_exception_if_hand_is_empty():
    with pytest.raises(Exception):
        check_hand("")

def test_flush():
    hand = "2H 3H 5H 6H 7H"
    assert check_hand(hand) == "Flush"
