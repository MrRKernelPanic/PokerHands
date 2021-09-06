from card import Card
from hand import Hand
from phands import PHand
from collections import Counter

def check_hand(raw_player_hands):
    _split = raw_player_hands.split("  ")
    raw_black_hand = _split[0].replace("Black: ","")
    raw_white_hand = _split[1].replace("White: ","")

    black_hand = Hand(raw_black_hand)
    black_hand.hand_colour = "Black"
    white_hand = Hand(raw_white_hand)
    white_hand.hand_colour = "White"

    black_poker_hand = black_hand.find_poker_hand()
    white_poker_hand = white_hand.find_poker_hand()
    
    hands_to_compare = [
                        black_hand,
                        white_hand
                        ]

    for hand_type in PHand:
        winners = []
        for hand in hands_to_compare:
            if hand.find_poker_hand() == hand_type.value:
                winners.append(hand)
        
        if len(winners) > 1: #Two hands the same
            print(winners)
            tie_breaker = max(hand.highest_card_in_tie_breaker for hand in winners)
            final_list = [hand for hand in winners if hand.highest_card_in_tie_breaker == tie_breaker]
            remainder_list = [hand for hand in winners if hand.highest_card_in_tie_breaker != tie_breaker]
            print(final_list)

            if len(final_list) == 1:
                return final_list[0].hand_colour + " wins, - with " + final_list[0].find_poker_hand() + ": " + str(final_list[0].highest_card_in_tie_breaker) + " over " + str(remainder_list[0].highest_card_in_tie_breaker)
            # else:
            #     for hand_type in PHand:
            #         winners2=[]
            #         for hand in final_list:
            #             if hand.find_poker_hand() == hand_type.value:
            #                 winners2.append(hand)
            #         if len(winners2) == 1:
            #             return winners2[0].hand_colour + " wins, - with " + winners2[0].find_poker_hand() + ": " + str(winners[0].remainder_hand_after_highest_poker_hand) + " over " + str(remainder_list[0].highest_card_in_tie_breaker)
            
            # print(len(pair_wins))

            # if len(pair_wins) == 1:
            #     print("a pair wins!")
            #     return pair_wins[0].hand_colour + " wins, - with " + pair_wins[0].remainder_hand_after_high_hand + ": " + str(pair_wins[0].highest_card_of_remaining_hand) + " over " + str(winners[0].highest_card_of_remaining_hand)
            # elif len(pair_wins) > 1:
            #     pair_wins.sort(items.highest_card_of_remaining_hand)
            #     print("working on this!")

            # if len(winners2) == 1:
            #     print("one winner!")
            #     #win2 = winners2[0]
            #     #win1 = winners[0]
            #     return winners2[0].hand_colour + " wins, - with " + hand_type.value + ": " + str(winners2[0].highest_card_in_tie_breaker) + " over " + str(winners[0].highest_card_in_tie_breaker)
            
            # if len(single_wins) == 1:
            #     print("single winner!")
            #     return single_wins[0].hand_colour + " wins, - with " + hand_type.value + ": " + str(single_wins[0].highest_card_of_remaining_hand) + " over " + str(winners[0].highest_card_of_remaining_hand)
            
            # else:
            #     print("second check")
            #     if black_hand.remainder_hand_after_high_hand == white_hand.remainder_hand_after_high_hand:
            #         if black_hand.highest_card_of_remaining_hand > white_hand.highest_card_of_remaining_hand:
            #             return "Black wins, - with " + black_hand.remainder_hand_after_high_hand + ": " + str(black_hand.highest_card_of_remaining_hand) + " over " + str(white_hand.highest_card_of_remaining_hand)
            #         elif black_hand.highest_card_of_remaining_hand < white_hand.highest_card_of_remaining_hand:
            #             return "White wins, - with " + white_hand.remainder_hand_after_high_hand + ": " + str(white_hand.highest_card_of_remaining_hand) + " over " + str(black_hand.highest_card_of_remaining_hand)
            #         else:
            #             return "Draw"
            #     elif white_hand.remainder_hand_after_high_hand == "a pair":
            #         return "White wins, - with " + white_hand.remainder_hand_after_high_hand + ": " + str(white_hand.highest_card_of_remaining_hand) + " over " + str(black_hand.highest_card_of_remaining_hand)
            #     else:
            #         return "Black wins, - with " + black_hand.remainder_hand_after_high_hand + ": " + str(black_hand.highest_card_of_remaining_hand) + " over " + str(white_hand.highest_card_of_remaining_hand)
            
        for hand in hands_to_compare:
            if hand_type.value == hand.find_poker_hand():
                return hand.hand_colour + " wins, - with " + hand.find_poker_hand()             
    return "Nobody Wins"

# def poker_hand_equal(hand, hand_to_check):
#     print(hand.find_poker_hand())
#     print(hand_to_check.value)
#     if hand.find_poker_hand() == hand_to_check.value:
       
#         return True
#     else:
#         return False