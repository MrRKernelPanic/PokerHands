import pytest
from poker_hands import check_hand


def test_raise_exception_if_hand_is_empty():
    with pytest.raises(Exception):
        check_hand("")

def test_flush():
    hand = "2H 3H 5H 6H 7H"
    assert check_hand(hand) == "Flush"

def test_4_of_a_kind():
    hand = "2H 7C 7D 7H 7S"
    assert check_hand(hand) == "4 of a kind"

def test_full_house():
    hand = "2H 2C 7C 7D 7S"
    assert check_hand(hand) == "Full house"

def test_3_of_a_kind():
    hand = "2H 4C 7C 7D 7S"
    assert check_hand(hand) == "3 of a kind"

def test_a_pair():
    hand = "2H 2C 1C 3C 4C"
    assert check_hand(hand) == "a pair"

def test_2_pairs():
    hand = "2H 2S 1C 3C 3H"
    assert check_hand(hand) == "2 pairs"

def test_can_handle_ten():
    hand = "10H 10C 10D 8C 10S"
    assert check_hand(hand) == "4 of a kind"

def test_straight():
    hand = "9H 10D JH QS KH"
    assert check_hand(hand) == "Straight"

def test_straight_flush():
    hand = "9H 10H JH QH KH"
    assert check_hand(hand) == "Straight Flush"

