from card import Card
from hand import Hand
from phands import PHand

def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    raw_black_hand = _split[0].replace("Black: ","")
    raw_white_hand = _split[1].replace("White: ","")

    black_hand = Hand(raw_black_hand)
    white_hand = Hand(raw_white_hand)
    
    black_poker_hand = black_hand.find_poker_hand()
    white_poker_hand = white_hand.find_poker_hand()
    
    hands_to_compare = {
                        "Black": black_poker_hand,
                        "White": white_poker_hand
                        }
    
    if black_poker_hand == white_poker_hand:
               
        if black_hand.highest_card_in_tie_breaker < white_hand.highest_card_in_tie_breaker:
            return "White wins, - with " + white_poker_hand + ": " + str(white_hand.highest_card_in_tie_breaker) + " over " + str(black_hand.highest_card_in_tie_breaker)
        elif black_hand.highest_card_in_tie_breaker == white_hand.highest_card_in_tie_breaker:
            if black_hand.remainder_hand_after_high_hand == "a pair" or white_hand.remainder_hand_after_high_hand == "a pair":
                if black_hand.remainder_hand_after_high_hand == white_hand.remainder_hand_after_high_hand:
                    if black_hand.highest_card_of_remaining_hand > white_hand.highest_card_of_remaining_hand:
                        return "Black wins, - with " + black_hand.remainder_hand_after_high_hand + ": " + str(black_hand.highest_card_of_remaining_hand) + " over " + str(white_hand.highest_card_of_remaining_hand)
                    elif black_hand.highest_card_of_remaining_hand < white_hand.highest_card_of_remaining_hand:
                        return "White wins, - with " + white_hand.remainder_hand_after_high_hand + ": " + str(white_hand.highest_card_of_remaining_hand) + " over " + str(black_hand.highest_card_of_remaining_hand)
                    else:
                        return "Draw"
                elif white_hand.remainder_hand_after_high_hand == "a pair":
                     return "White wins, - with " + white_hand.remainder_hand_after_high_hand + ": " + str(white_hand.highest_card_of_remaining_hand) + " over " + str(black_hand.highest_card_of_remaining_hand)
                else:
                    return "Black wins, - with " + black_hand.remainder_hand_after_high_hand + ": " + str(black_hand.highest_card_of_remaining_hand) + " over " + str(white_hand.highest_card_of_remaining_hand)
            else:
                if black_hand.highest_card_of_remaining_hand > white_hand.highest_card_of_remaining_hand:
                    return "Black wins, - with " + str(black_hand.remainder_hand_after_high_hand) + ": " + str(black_hand.highest_card_of_remaining_hand) + " over " + str(white_hand.highest_card_of_remaining_hand)
                elif black_hand.highest_card_of_remaining_hand < white_hand.highest_card_of_remaining_hand:
                    return "White wins, - with " + str(white_hand.remainder_hand_after_high_hand) + ": " + str(white_hand.highest_card_of_remaining_hand) + " over " + str(black_hand.highest_card_of_remaining_hand)
                else:
                    return "Draw2"

        else:
            return "Black wins, - with " + black_poker_hand + ": " + str(black_hand.highest_card_in_tie_breaker) + " over " + str(white_hand.highest_card_in_tie_breaker)

    for hand_type in PHand:
        for key, value in hands_to_compare.items():
            if hand_type.value == value:
                return key + " wins, - with " + value             
    return "Nobody Wins"
    