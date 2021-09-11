import pytest
from hand import Hand

def test_flush():
    hand = Hand("2H 3H 5H 6H 7H", "Black")
    assert hand.find_poker_hand() == "Flush"

def test_4_of_a_kind():
    hand = Hand("2H 7C 7D 7H 7S", "Black")
    assert hand.find_poker_hand() == "4 of a kind"

def test_full_house():
    hand = Hand("3H 3C 3D 9H 9C", "Black")
    assert hand.find_poker_hand() == "Full house"

def test_3_of_a_kind():
    hand = Hand("2H 4C 7C 7D 7S", "Black")
    assert hand.find_poker_hand() == "3 of a kind"

def test_a_pair():
    hand = Hand("2H 2C 1C 3C 4C", "Black")
    assert hand.find_poker_hand() == "a pair"

def test_2_pairs():
    hand = Hand("2H 2S 1C 3C 3H", "White")
    assert hand.find_poker_hand() == "2 pairs"

def test_can_handle_ten():
    hand = Hand("TH TC TD 8C 10S", "Black")
    assert hand.find_poker_hand() == "4 of a kind"

def test_straight():
    hand = Hand("9H TD JH QS KH", "Black")
    assert hand.find_poker_hand() == "Straight"

def test_straight_flush():
    hand = Hand("9H TH JH QH KH", "White")
    assert hand.find_poker_hand() == "Straight Flush"
