from card import Card
from hand import Hand
from phands import PHand

def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    hands_to_compare = []
    for hands in _split:
        _colour = hands.split(':')[0]
        _raw_hand = hands.replace(_colour + ": ","")        
        _make_hand = Hand(_raw_hand, _colour)
        hands_to_compare.append(_make_hand)
    
    for hand_type in PHand:
        winners_first_pass = []
        for hand in hands_to_compare:
            if hand.find_poker_hand() == hand_type.value:
                winners_first_pass.append(hand)
        if len(winners_first_pass) > 1: 
            if deal_with_draws (winners_first_pass) != "":
                return(deal_with_draws(winners_first_pass))
        elif len(winners_first_pass) == 1:    
            return winners_first_pass[0].hand_colour + " wins, - with " + winners_first_pass[0].find_poker_hand()                
    return "Nobody Wins"

def deal_with_draws(draw_hands):
    tie_breaker = max(hand.highest_card_in_tie_breaker for hand in draw_hands)
    winners_second_pass = [hand for hand in draw_hands if hand.highest_card_in_tie_breaker == tie_breaker]
    losers_first_pass = [hand for hand in draw_hands if hand.highest_card_in_tie_breaker != tie_breaker]
    
    if len(winners_second_pass) == 1:
        return winners_second_pass[0].hand_colour + " wins, - with " + winners_second_pass[0].find_poker_hand() + ": " + str(winners_second_pass[0].highest_card_in_tie_breaker) + " over " + str(losers_first_pass[0].highest_card_in_tie_breaker)
    else:
        if deal_with_draws_2nd_pass(winners_second_pass) != "":
            return deal_with_draws_2nd_pass(winners_second_pass)
            

def deal_with_draws_2nd_pass(pass_hands):
    for hand_type in PHand:
        tie_breaker = max(hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) for hand in pass_hands)
        winners_final_pass = [hand for hand in pass_hands if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) == tie_breaker]
        losers_second_pass = [hand for hand in pass_hands if hand.remainder_high_card_after_high_hand(hand.dict_high_card_lookup.get(hand.phand)) != tie_breaker]
        
        if len(winners_final_pass) == 1:
            return (winners_final_pass[0].hand_colour + " wins, - with " + winners_final_pass[0].find_poker_hand()
            + ": " + str(winners_final_pass[0].remainder_high_card_after_high_hand(winners_final_pass[0].dict_high_card_lookup.get(winners_final_pass[0].phand)))
            + " over " + str(losers_second_pass[0].remainder_high_card_after_high_hand(losers_second_pass[0].dict_high_card_lookup.get(losers_second_pass[0].phand))))
        else:

            if hand_type.value == "a pair":
                if second_pair_check(winners_final_pass) != "":
                    return second_pair_check(winners_final_pass)

            if sequential_card_check(winners_final_pass) != "":
                return sequential_card_check(winners_final_pass)
            else:
                return "Tie"

def sequential_card_check(seq_hands):
    for sequential_cards in range(0,5):
        if seq_hands[0].card_values[sequential_cards] != seq_hands[1].card_values[sequential_cards]:
            if seq_hands[0].card_values[sequential_cards] > seq_hands[1].card_values[sequential_cards]:
                return (seq_hands[0].hand_colour + " wins, - with " + seq_hands[0].find_poker_hand()
                    + ": " + str(seq_hands[0].card_values[sequential_cards])
                    + " over " + str(seq_hands[1].card_values[sequential_cards]))
            elif seq_hands[0].card_values[sequential_cards] < seq_hands[0].card_values[sequential_cards]:
                return (seq_hands[1].hand_colour + " wins, - with " + seq_hands[1].find_poker_hand()
                    + ": " + str(seq_hands[1].card_values[sequential_cards])
                    + " over " + str(seq_hands[0].card_values[sequential_cards]))
        

def second_pair_check(pair_hands):
    if pair_hands[0].two_pair_last_card_value > pair_hands[1].two_pair_last_card_value:
        return (pair_hands[0].hand_colour + " wins, - with " + pair_hands[0].find_poker_hand()
            + ": " + str(pair_hands[0].two_pair_last_card_value)
            + " over " + str(pair_hands[1].two_pair_last_card_value))
    elif pair_hands[0].two_pair_last_card_value > pair_hands[1].two_pair_last_card_value:
        return (pair_hands[1].hand_colour + " wins, - with " + pair_hands[1].find_poker_hand()
            + ": " + str(pair_hands[1].two_pair_last_card_value)
            + " over " + str(pair_hands[0].two_pair_last_card_value))
    
