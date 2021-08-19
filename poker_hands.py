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

        high_black = 0
        high_white = 0

        if black_poker_hand == white_poker_hand:

            if black_poker_hand == "the highest card" or black_poker_hand == "Flush" or black_poker_hand == "Straight Flush":
                high_black = highest_card_in_poker_hand(black_hand, 1)
                high_white = highest_card_in_poker_hand(white_hand, 1)
               
            if (black_poker_hand == "2 pairs") or (black_poker_hand == "a pair"):
            
                high_black = highest_card_in_poker_hand(black_hand, 2)
                high_white = highest_card_in_poker_hand(white_hand, 2)

            if black_poker_hand == "3 of a kind" or black_poker_hand == "Full house":
                
                high_black = highest_card_in_poker_hand(black_hand, 3)
                high_white = highest_card_in_poker_hand(white_hand, 3)
            
            if black_poker_hand == "4 of a kind":
                
                high_black = highest_card_in_poker_hand(black_hand, 4)
                high_white = highest_card_in_poker_hand(white_hand, 4)
            
                   
            if high_black < high_white:
                return "White wins, - with " + white_poker_hand + ": " + str(high_white) + " over " + str(high_black)
            elif high_black == high_white:
                return "Draw"
            else:
                return "Black wins, - with " + black_poker_hand + ": " + str(high_black) + " over " + str(high_white)

        for key, value in hands_to_compare.items():
            if hand_type == value:
                return key + " wins, - with " + value             
    return "Nobody Wins"

def highest_card_in_poker_hand(player_hand, num_of_a_kind):
    high_card_value = 0
    for each_card in player_hand.card_values:
                count = player_hand.card_values.count(each_card)
                if count == num_of_a_kind:
                    if each_card >= high_card_value:
                        high_card_value = each_card
    return high_card_value