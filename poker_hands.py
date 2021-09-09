from card import Card
from hand import Hand
from phands import PHand
from collections import Counter

def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    raw_black_hand = _split[0].replace("Black: ","")
    raw_white_hand = _split[1].replace("White: ","")

    black_hand = Hand(raw_black_hand, "Black")
    white_hand = Hand(raw_white_hand, "White")
   
    hands_to_compare = [
                        black_hand,
                        white_hand
                        ]

    for hand_type in PHand:
        winners = []
        for hand in hands_to_compare:
            if hand.find_poker_hand() == hand_type.value:
                winners.append(hand)
        
        if len(winners) > 1: 
            tie_breaker = max(hand.highest_card_in_tie_breaker for hand in winners)
            final_list = [hand for hand in winners if hand.highest_card_in_tie_breaker == tie_breaker]
            remainder_list = [hand for hand in winners if hand.highest_card_in_tie_breaker != tie_breaker]
            
            if len(final_list) == 1:
                return final_list[0].hand_colour + " wins, - with " + final_list[0].find_poker_hand() + ": " + str(final_list[0].highest_card_in_tie_breaker) + " over " + str(remainder_list[0].highest_card_in_tie_breaker)
            else:
                for hand_type in PHand:
                    tie_breaker = max(hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) for hand in final_list)
                    final_list2 = [hand for hand in final_list if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) == tie_breaker]
                    remainder_list2 = [hand for hand in final_list if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) != tie_breaker]
                    
                    if len(final_list2) == 1:
                        return (final_list2[0].hand_colour + " wins, - with " + final_list2[0].find_poker_hand()
                        + ": " + str(final_list2[0].remainder_high_card_after_high_hand(final_list2[0].dict_high_card_lookup.get(final_list2[0].phand)))
                        + " over " + str(remainder_list2[0].remainder_high_card_after_high_hand(remainder_list2[0].dict_high_card_lookup.get(remainder_list2[0].phand))))
                    else:
                        return ("Tie")    
            
        for hand in hands_to_compare:
            if hand_type.value == hand.find_poker_hand():
                return hand.hand_colour + " wins, - with " + hand.find_poker_hand()             
    return "Nobody Wins"
