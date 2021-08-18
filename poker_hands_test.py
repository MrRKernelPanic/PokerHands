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

def test_straight_white_wins():
    test_hand = "Black: 1C 2S 3H 4D 7C  White: 3C 4D 5S 6C 7D"
    assert check_hand(test_hand) == "White wins, - with Straight"

def test_three_of_a_kind_black_wins():
    test_hand = "Black: 2C 2D 2H 9C 8D  White: 2D 3D 4D 9S 9H"
    assert check_hand(test_hand) == "Black wins, - with 3 of a kind"

def test_two_pairs_white_wins():
    test_hand = "Black: 2C 2D 9C 8C 7S  White: 2S 2H 4S 4C JC"
    assert check_hand(test_hand) == "White wins, - with 2 pairs"

def test_a_pair_black_wins():
    test_hand = "Black: 2C 2D 9C 8C 7S  White: 2S 1H 4S 3H JH"
    assert check_hand(test_hand) == "Black wins, - with a pair"

def test_highest_card_white_wins():
    test_hand = "Black: 2C 3D 9C 8C 7S  White: 3C 4D 10C 9H 8H"
    assert check_hand(test_hand) == "White wins, - with high card: 10 over 9"

def test_highest_card_black_wins():
    test_hand = "Black: 2C 3D JC 8C 7S  White: 3C 4D 9C 2H 8H"
    assert check_hand(test_hand) == "Black wins, - with high card: 11 over 9"

def test_highest_card_draw():
    test_hand = "Black: 2C 3D JC 8C 7S  White: 3C 4D 9C JH 8H"
    assert check_hand(test_hand) == "Draw"

def test_each_player_has_2_pairs_highest_white_wins():
    test_hand = "Black: 2C 2D 4H 4S 10H  White: 3C 3C 5H 5C JS"
    assert check_hand(test_hand) == "White wins, - with 2 pairs: 5 over 4"

def test_each_player_has_2_pairs_highest_black_wins():
    test_hand = "Black: 3C 3C 5H 5C JS  White: 2C 2D 4H 4S 10H"
    assert check_hand(test_hand) == "Black wins, - with 2 pairs: 5 over 4"

def test_each_player_has_a_pair_highest_white_wins():
    test_hand = "Black: 1C 2D 4H 4S 10H  White: 2C 3C 5H 5C JS"
    assert check_hand(test_hand) == "White wins, - with a pair: 5 over 4"

def test_each_player_has_3_of_a_kind_black_wins():
    test_hand = "Black: 8C 8D 8H 9S 7D  White: 2C 2D 2H 9D 7S"
    assert check_hand(test_hand) == "Black wins, - with 3 of a kind: 8 over 2"