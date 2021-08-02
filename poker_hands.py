from card import Card


def check_hand(hand):    
    cards = hand.split(" ")

    hand_of_cards = []
    for card in cards:
        hand_of_cards.append(Card(card))

    unique_values = {}
    unique_suits = {}

    for card in hand_of_cards:
        if card.value not in unique_suits.keys():
            unique_suits[card.suit] = 1
        else:
            unique_suits[card.suit] += 1

        if card.value not in unique_values.keys():
            unique_values[card.value] = 1
        else:
            unique_values[card.value] += 1
    
    if len(unique_suits) == 1:
        return "Flush"

    if unique_values[max(unique_values)] == 4:
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

