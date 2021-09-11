import pytest
from poker_hands import check_hand

def test_straight_flush_wins():
    test_hand = "Black: 2H 3D 5S 9C KD  White: 2H 3H 4H 5H 6H"
    assert check_hand(test_hand) == "White wins, - with Straight Flush"

def test_4_of_a_kind_black_wins():
    test_hand = "Black: TH TC TD 8C TS  White: 3H 3D 3C 2H 1H"
    assert check_hand(test_hand) == "Black wins, - with 4 of a kind"

def test_full_house_black_wins():
    test_hand = "Black: 2H 2C 7C 7D 7S  White: 3H 3C 3D 9H 8C"
    assert check_hand(test_hand) == "Black wins, - with Full house"

def test_flush_white_wins():
    test_hand = "Black: 1C 2S 3H 4D 7C  White: 3H 4H 5H 7H TH"
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
    test_hand = "Black: 2C 3D 9C 8C 7S  White: 3C 4D TC 9H 8H"
    assert check_hand(test_hand) == "White wins, - with the highest card: 10 over 9"

def test_highest_card_black_wins():
    test_hand = "Black: 2C 3D JC 8C 7S  White: 3C 4D 9C 2H 8H"
    assert check_hand(test_hand) == "Black wins, - with the highest card: 11 over 9"

def test_highest_card_draw():
    test_hand = "Black: 2C 3D JC 8C 7S  White: 3C 4D 9C JH 8H"
    assert check_hand(test_hand) == "White wins, - with the highest card: 9 over 8"

def test_each_player_has_2_pairs_highest_white_wins():
    test_hand = "Black: 2C 2D 4H 4S TH  White: 3C 3C 5H 5C JS"
    assert check_hand(test_hand) == "White wins, - with 2 pairs: 5 over 4"

def test_each_player_has_2_pairs_highest_black_wins():
    test_hand = "Black: 3C 3C 5H 5C JS  White: 2C 2D 4H 4S TH"
    assert check_hand(test_hand) == "Black wins, - with 2 pairs: 5 over 4"

def test_each_player_has_a_pair_highest_white_wins():
    test_hand = "Black: 1C 2D 4H 4S TH  White: 2C 3C 5H 5C JS"
    assert check_hand(test_hand) == "White wins, - with a pair: 5 over 4"

def test_each_player_has_3_of_a_kind_black_wins():
    test_hand = "Black: 8C 8D 8H 9S 7D  White: 2C 2D 2H 9D 7S"
    assert check_hand(test_hand) == "Black wins, - with 3 of a kind: 8 over 2"

def test_each_player_has_4_of_a_kind_black_wins():
    test_hand = "Black: 8C 8D 8H 8S 7D  White: 2C 2D 2H 2D 7S"
    assert check_hand(test_hand) == "Black wins, - with 4 of a kind: 8 over 2"

def test_each_player_has_full_house_white_wins():
    test_hand = "Black: 8C 8D 8H 7S 7D  White: 9C 9D 9H 7C 7H"
    assert check_hand(test_hand) == "White wins, - with Full house: 9 over 8"

def test_each_player_has_flush_white_wins():
    test_hand = "Black: 3S 2S 4S 5S 7S  White: KH 7H 8H 9H TH JH"
    assert check_hand(test_hand) == "White wins, - with Flush: 13 over 7"

def test_each_player_has_flush_black_wins():
    test_hand = "Black: QH 8H 9H 10H JH  White: 3S 2S 4S 5S 6S"
    assert check_hand(test_hand) == "Black wins, - with Straight Flush: 12 over 6"

def test_tie_two_pairs():
    test_hand = "Black: 5H 5C 3H 3C JS  White: 5S 5D 4H 4C TS"
    assert check_hand(test_hand) == "White wins, - with 2 pairs: 4 over 3"

# Extremely Unlikely Cases.
def test_tie_two_pairs_highest_card_match():
     test_hand = "Black: 5H 5C 4H 4C JS  White: 5S 5D 4D 4S TS"
     assert check_hand(test_hand) == "Black wins, - with 2 pairs: 11 over 10"

def test_a_pair_and_highest_card_match():
    test_hand = "Black: 6H 6C 5H 4C 2S  White: 6S 6D 5D 3S 2D"
    assert check_hand(test_hand) == "Black wins, - with a pair: 4 over 3"
