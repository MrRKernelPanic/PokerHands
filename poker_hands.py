from card import Card
from hand import Hand
from enum import Enum

class PHand(Enum):
    STRAIGHT_FLUSH = "Straight Flush"
    FOUR_OF_A_KIND ="4 of a kind"
    FULL_HOUSE = "Full house"
    FLUSH = "Flush"
    STRAIGHT = "Straight"
    THREE_UF_A_KIND = "3 of a kind"
    TWO_PAIRS = "2 pairs"
    A_PAIR = "a pair"
    HIGH_CARD = "the highest card"

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
    high_black = 0
    high_white = 0

    if black_poker_hand == white_poker_hand:

        if black_poker_hand == PHand.HIGH_CARD.value or black_poker_hand == PHand.FLUSH.value or black_poker_hand == PHand.STRAIGHT_FLUSH.value:
            high_black = highest_card_in_poker_hand(black_hand, 1)
            high_white = highest_card_in_poker_hand(white_hand, 1)
        
        if black_poker_hand == PHand.TWO_PAIRS.value or black_poker_hand == PHand.A_PAIR.value:
        
            high_black = highest_card_in_poker_hand(black_hand, 2)
            high_white = highest_card_in_poker_hand(white_hand, 2)

        if black_poker_hand == PHand.THREE_UF_A_KIND.value or black_poker_hand == PHand.FULL_HOUSE.value:
            
            high_black = highest_card_in_poker_hand(black_hand, 3)
            high_white = highest_card_in_poker_hand(white_hand, 3)
        
        if black_poker_hand == PHand.FOUR_OF_A_KIND.value:
            
            high_black = highest_card_in_poker_hand(black_hand, 4)
            high_white = highest_card_in_poker_hand(white_hand, 4)
        
            
        if high_black < high_white:
            return "White wins, - with " + white_poker_hand + ": " + str(high_white) + " over " + str(high_black)
        elif high_black == high_white:
            return "Draw"
        else:
            return "Black wins, - with " + black_poker_hand + ": " + str(high_black) + " over " + str(high_white)


    for hand_type in PHand:

        # high_black = 0
        # high_white = 0

        # if black_poker_hand == white_poker_hand:

        #     if black_poker_hand == PHand.HIGH_CARD or black_poker_hand == PHand.FLUSH or black_poker_hand == PHand.STRAIGHT_FLUSH:
        #         high_black = highest_card_in_poker_hand(black_hand, 1)
        #         high_white = highest_card_in_poker_hand(white_hand, 1)
               
        #     if black_poker_hand == PHand.TWO_PAIRS or black_poker_hand == PHand.A_PAIR:
            
        #         high_black = highest_card_in_poker_hand(black_hand, 2)
        #         high_white = highest_card_in_poker_hand(white_hand, 2)

        #     if black_poker_hand == PHand.THREE_UF_A_KIND or black_poker_hand == PHand.FULL_HOUSE:
                
        #         high_black = highest_card_in_poker_hand(black_hand, 3)
        #         high_white = highest_card_in_poker_hand(white_hand, 3)
            
        #     if black_poker_hand == PHand.FOUR_OF_A_KIND:
                
        #         high_black = highest_card_in_poker_hand(black_hand, 4)
        #         high_white = highest_card_in_poker_hand(white_hand, 4)
            
                   
        #     if high_black < high_white:
        #         return "White wins, - with " + white_poker_hand + ": " + str(high_white) + " over " + str(high_black)
        #     elif high_black == high_white:
        #         return "Draw"
        #     else:
        #         return "Black wins, - with " + black_poker_hand + ": " + str(high_black) + " over " + str(high_white)

        for key, value in hands_to_compare.items():
            if hand_type.value == value:
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