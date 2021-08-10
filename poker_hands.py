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
    
    hand_types = ["Straight Flush", "4 of a kind", "Full house"]

    winner = "Nobody"
    winning_hand = ""

    for hand_type in hand_types:
        if white_poker_hand == hand_type or black_poker_hand == hand_type:
            if white_poker_hand == hand_type:
                winner = "White"
                winning_hand =  white_poker_hand
                break
            else:
                winner = "Black"
                winning_hand =  black_poker_hand
                break
    print(winning_hand)            
    return winner + " wins, - with " + winning_hand
    