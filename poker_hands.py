from card import Card
from hand import Hand


def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    raw_black_hand = _split[0].replace("Black: ","")
    raw_white_hand = _split[1].replace("White: ","")

    black_hand = Hand(raw_black_hand)
    white_hand = Hand(raw_white_hand)
    
    black_poker_hand = black_hand.find_poker_hand()
    white_poker_hand = white_hand.find_poker_hand()
    
    print(white_poker_hand)
    print(black_poker_hand)

    if white_poker_hand == "Straight Flush":
        return "White wins, - with " + white_poker_hand
    if black_poker_hand == "4 of a kind":
        return "Black wins, - with " + black_poker_hand
    if black_poker_hand == "Full house":
        return "Black wins, - with " + black_poker_hand
    raise Exception
