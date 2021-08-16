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
    
    hand_types = ["Straight Flush", "4 of a kind", "Full house", "Flush", "Straight"]

    hands_to_compare = {
                        "Black": black_poker_hand,
                        "White": white_poker_hand
                        }
                        
    for hand_type in hand_types:
        for key, value in hands_to_compare.items():
            if hand_type == value:
                return key + " wins, - with " + value             

    return "Nobody Wins"
