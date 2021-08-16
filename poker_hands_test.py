import pytest
from poker_hands import check_hand

def test_straight_flush_wins():
    test_hand = "Black: 2H 3D 5S 9C KD  White: 2H 3H 4H 5H 6H"
    assert check_hand(test_hand) == "White wins, - with Straight Flush"

def test_4_of_a_kind_black_wins():
    test_hand = "Black: 10H 10C 10D 8C 10S  White: 3H 3D 3C 2H 1H"
    assert check_hand(test_hand) == "Black wins, - with 4 of a kind"

def test_full_house_black_wins():
    test_hand = "Black: 2H 2C 7C 7D 7S  White: 3H 3C 3D 9H 8C"
    assert check_hand(test_hand) == "Black wins, - with Full house"

def test_flush_white_wins():
    test_hand = "Black: 1C 2S 3H 4D 7C  White: 3H 4H 5H 7H 10H"
    assert check_hand(test_hand) == "White wins, - with Flush"