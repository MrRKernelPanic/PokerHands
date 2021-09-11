from card import Card
from hand import Hand
from phands import PHand
#from collections import Counter

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
        winners_first_pass = []
        for hand in hands_to_compare:
            if hand.find_poker_hand() == hand_type.value:
                winners_first_pass.append(hand)
        
        if len(winners_first_pass) > 1: 
            tie_breaker = max(hand.highest_card_in_tie_breaker for hand in winners_first_pass)
            winners_second_pass = [hand for hand in winners_first_pass if hand.highest_card_in_tie_breaker == tie_breaker]
            losers_first_pass = [hand for hand in winners_first_pass if hand.highest_card_in_tie_breaker != tie_breaker]
            
            if len(winners_second_pass) == 1:
                return winners_second_pass[0].hand_colour + " wins, - with " + winners_second_pass[0].find_poker_hand() + ": " + str(winners_second_pass[0].highest_card_in_tie_breaker) + " over " + str(losers_first_pass[0].highest_card_in_tie_breaker)
            else:
                for hand_type in PHand:
                    tie_breaker = max(hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) for hand in winners_second_pass)
                    winners_final_pass = [hand for hand in winners_second_pass if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) == tie_breaker]
                    losers_second_pass = [hand for hand in winners_second_pass if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) != tie_breaker]
                    
                    if len(winners_final_pass) == 1:
                        return (winners_final_pass[0].hand_colour + " wins, - with " + winners_final_pass[0].find_poker_hand()
                        + ": " + str(winners_final_pass[0].remainder_high_card_after_high_hand(winners_final_pass[0].dict_high_card_lookup.get(winners_final_pass[0].phand)))
                        + " over " + str(losers_second_pass[0].remainder_high_card_after_high_hand(losers_second_pass[0].dict_high_card_lookup.get(losers_second_pass[0].phand))))
                    else:

                        if hand_type.value == "a pair":
                            if winners_final_pass[0].two_pair_last_card_value > winners_final_pass[1].two_pair_last_card_value:
                                return (winners_final_pass[0].hand_colour + " wins, - with " + winners_final_pass[0].find_poker_hand()
                                    + ": " + str(winners_final_pass[0].two_pair_last_card_value)
                                    + " over " + str(winners_final_pass[1].two_pair_last_card_value))
                            elif winners_final_pass[0].two_pair_last_card_value > winners_final_pass[1].two_pair_last_card_value:
                                return (winners_final_pass[1].hand_colour + " wins, - with " + winners_final_pass[1].find_poker_hand()
                                    + ": " + str(winners_final_pass[1].two_pair_last_card_value)
                                    + " over " + str(winners_final_pass[0].two_pair_last_card_value))
                            for sequential_cards in range(0,5):
                                if winners_final_pass[0].card_values[sequential_cards] != winners_final_pass[1].card_values[sequential_cards]:
                                    if winners_final_pass[0].card_values[sequential_cards] > winners_final_pass[1].card_values[sequential_cards]:
                                        return (winners_final_pass[0].hand_colour + " wins, - with " + winners_final_pass[0].find_poker_hand()
                                            + ": " + str(winners_final_pass[0].card_values[sequential_cards])
                                            + " over " + str(winners_final_pass[1].card_values[sequential_cards]))
                                    elif winners_final_pass[0].card_values[sequential_cards] < winners_final_pass[0].card_values[sequential_cards]:
                                        return (winners_final_pass[1].hand_colour + " wins, - with " + winners_final_pass[1].find_poker_hand()
                                            + ": " + str(winners_final_pass[1].card_values[sequential_cards])
                                            + " over " + str(winners_final_pass[0].card_values[sequential_cards]))
                            return ("Tie")





        elif len(winners_first_pass) == 1:    
            return winners_first_pass[0].hand_colour + " wins, - with " + winners_first_pass[0].find_poker_hand()                
    return "Nobody Wins"
