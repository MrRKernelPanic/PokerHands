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
    
    hand_types = ["Straight Flush", "4 of a kind", "Full house", "Flush", "Straight", "3 of a kind", "2 pairs", "a pair", "high card"]

    hands_to_compare = {
                        "Black": black_poker_hand,
                        "White": white_poker_hand
                        }
                        
    for hand_type in hand_types:
        if black_poker_hand == "high card" and white_poker_hand == "high card":
            if white_hand.get_max_card_value() > black_hand.get_max_card_value():
                return "White wins, - with " + white_poker_hand + ": " + str(white_hand.get_max_card_value())
            elif white_hand.get_max_card_value() == black_hand.get_max_card_value():
                return "Draw"
            else:
                return "Black wins, - with " + black_poker_hand + ": " + str(black_hand.get_max_card_value())

        if (black_poker_hand == "2 pairs" and white_poker_hand == "2 pairs") or (black_poker_hand == "a pair" and white_poker_hand == "a pair"):

            high_black = 0
            high_white = 0
            
            for each_card in black_hand.card_values:
                count = black_hand.card_values.count(each_card)
                if count == 2:
                    if each_card >= high_black:
                        high_black = each_card

            for each_card in white_hand.card_values:
                count = white_hand.card_values.count(each_card)
                if count == 2:
                    if each_card >= high_white:
                        high_white = each_card

            if high_black < high_white:
                return "White wins, - with " + white_poker_hand + ": " + str(high_white) + " over " + str(high_black)
            elif high_black == high_white:
                return "not implemented yet"
            else:
                return "Black wins, - with " + black_poker_hand + ": " + str(high_black) + " over " + str(high_white)

        for key, value in hands_to_compare.items():
            if hand_type == value:
                return key + " wins, - with " + value             
    return "Nobody Wins"
