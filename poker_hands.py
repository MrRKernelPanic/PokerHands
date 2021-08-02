from card import Card
from hand import Hand


def check_hand(raw_hand):    
    hand = Hand(raw_hand)
    unique_values = {}
    unique_suits = {}
    max_card_num_value = 0
    min_card_num_value = 15

    for card in hand.cards:
        if card.value not in unique_suits.keys():
            unique_suits[card.suit] = 1
        else:
            unique_suits[card.suit] += 1

        if card.value not in unique_values.keys():
            unique_values[card.value] = 1
        else:
            unique_values[card.value] += 1
        
        if card.value < min_card_num_value:
            min_card_num_value = card.value

        if card.value > max_card_num_value:
            max_card_num_value = card.value

    #print(max_card)
    #print(min_card)

    if len(unique_suits) == 1:
        if max_card_num_value - min_card_num_value == 4:
            return "Straight Flush"
        else:
            return "Flush"

    if max_card_num_value - min_card_num_value == 4:
            return "Straight"

    if unique_values[max(unique_values, key = unique_values.get)] == 4:
        return "4 of a kind"
    elif unique_values[max(unique_values)] == 3 and unique_values[min(unique_values)] == 2:
        return "Full house"
    elif unique_values[max(unique_values)] == 3 and unique_values[min(unique_values)] == 1:
        return "3 of a kind"
    elif unique_values[max(unique_values, key=unique_values.get)] == 2:
        pair_count = 0
        for key in unique_values:
            if unique_values[key] == 2:
                pair_count += 1
        
        if pair_count == 1:
            return "a pair"
        else:
            return "2 pairs"


    raise Exception
