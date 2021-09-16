from card import Card
from hand import Hand
from phands import PHand


def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    hands_to_compare = []
    all_cards_dealt = ""
    for hands in _split:
        _colour = hands.split(':')[0]
        _raw_hand = hands.replace(_colour + ": ", "")
        _make_hand = Hand(_raw_hand, _colour)
        all_cards_dealt += " " + _raw_hand
        hands_to_compare.append(_make_hand)
    _cards_dealt = all_cards_dealt[1:].split(' ')

    if len(hands_to_compare) > 10:
        return ("Too many hands to calculate")

    if check_duplicate_cards_dealt(_cards_dealt) != "":
        return check_duplicate_cards_dealt(_cards_dealt)

    if check_for_winner(hands_to_compare) != "":
        return check_for_winner(hands_to_compare)


def check_for_winner(_hands_to_compare):
    for hand_type in PHand:
        winners_first_pass = []
        for hand in _hands_to_compare:
            if hand.find_poker_hand() == hand_type.value:
                winners_first_pass.append(hand)
        if len(winners_first_pass) > 1:
            if deal_with_draws(winners_first_pass) != "":
                return deal_with_draws(winners_first_pass)
        elif len(winners_first_pass) == 1:
            return construct_win_msg(winners_first_pass[0], "", "win")


def deal_with_draws(draw_hands):
    tie_breaker = max(hand.highest_card_in_tie_breaker for hand in draw_hands)
    winners_second_pass = [
        hand for hand in draw_hands
        if hand.highest_card_in_tie_breaker
        == tie_breaker
        ]
    losers_first_pass = [
        hand for hand in draw_hands
        if hand.highest_card_in_tie_breaker
        != tie_breaker
        ]
    if len(winners_second_pass) == 1:
        return construct_win_msg(winners_second_pass[0],
                                 losers_first_pass[0],
                                 "win_1st_pass")
    else:
        if deal_with_draws_2nd_pass(winners_second_pass) != "":
            return deal_with_draws_2nd_pass(winners_second_pass)


def deal_with_draws_2nd_pass(pass_hands):
    for hand_type in PHand:
        tie_breaker = max(
            hand.remainder_high_card_after_high_hand(
                hand.dict_high_card_lookup.get(hand.phand))
            for hand in pass_hands)
        winners_final_pass = [
                            hand for hand in pass_hands
                            if hand.remainder_high_card_after_high_hand(
                                hand.dict_high_card_lookup.get(hand.phand))
                            == tie_breaker
                        ]
        losers_second_pass = [
                            hand for hand in pass_hands
                            if hand.remainder_high_card_after_high_hand(
                                hand.dict_high_card_lookup.get(hand.phand))
                            != tie_breaker
            ]
        if len(winners_final_pass) == 1:
            return construct_win_msg(winners_final_pass[0],
                                     losers_second_pass[0],
                                     "win_2nd_pass")
        else:
            if hand_type.value == "a pair":
                if second_pair_check(winners_final_pass) != "":
                    return second_pair_check(winners_final_pass)
            if sequential_card_check(winners_final_pass) != "":
                return sequential_card_check(winners_final_pass)
            else:
                return "Tie"


def sequential_card_check(seq_hands):
    for sequential_cards in range(0, 5):
        if seq_hands[0].card_values[sequential_cards]\
         != seq_hands[1].card_values[sequential_cards]:
            if seq_hands[0].card_values[sequential_cards]\
             > seq_hands[1].card_values[sequential_cards]:
                return construct_win_msg(seq_hands[0], seq_hands[1],
                                         "win_seq", sequential_cards)
            elif seq_hands[0].card_values[sequential_cards]\
                    < seq_hands[0].card_values[sequential_cards]:
                return construct_win_msg(seq_hands[1], seq_hands[0],
                                         "win_seq", sequential_cards)
    return "Tie"


def second_pair_check(pair_hands):
    if pair_hands[0].two_pair_last_card_value\
     > pair_hands[1].two_pair_last_card_value:
        return construct_win_msg(pair_hands[0], pair_hands[1], "win_2nd_pair")
    elif pair_hands[0].two_pair_last_card_value\
            > pair_hands[1].two_pair_last_card_value:
        return construct_win_msg(pair_hands[1], pair_hands[0], "win_2nd_pair")


def check_duplicate_cards_dealt(sent_cards):
    for card in sent_cards:
        if sent_cards.count(card) > 1:
            return "Matching Cards found in hands"
    return ""


def construct_win_msg(winner, loser, win_type, card_index=-1):
    mid_str = " wins, - with "
    base_str = winner.hand_colour + mid_str + winner.find_poker_hand()
    final_str = ""

    if win_type == "win":
        final_str = base_str
    elif win_type == "win_1st_pass":
        final_str = (base_str
                     + ": "
                     + str(winner.highest_card_in_tie_breaker)
                     + " over " + str(loser.highest_card_in_tie_breaker))
    elif win_type == "win_2nd_pass":
        final_str = (base_str
                     + ": " + str(winner.remainder_high_card_after_high_hand(
                      winner.dict_high_card_lookup.get(winner.phand)))
                     + " over " + str(loser.remainder_high_card_after_high_hand(
                      loser.dict_high_card_lookup.get(loser.phand))))
    elif win_type == "win_2nd_pair":
        final_str = (base_str
                     + ": " + str(winner.two_pair_last_card_value)
                     + " over " + str(loser.two_pair_last_card_value))
    elif win_type == "win_seq":
        final_str = (base_str
                     + ": " + str(winner.card_values[card_index])
                     + " over " + str(loser.card_values[card_index]))

    final_str = put_back_face_cards(final_str)
    return final_str


def put_back_face_cards(temp_string):
    card_num_value = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }
    for key, value in card_num_value.items():
        temp_string = temp_string.replace(str(value), key)
    return temp_string
