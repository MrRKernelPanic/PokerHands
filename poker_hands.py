from card import Card


def check_hand(hand):
    hearts = hand.count("H")   
    spades = hand.count("S")
    clubs = hand.count("C")
    diamonds = hand.count("D")

    if hearts == 5 or spades == 5 or clubs == 5 or diamonds == 5:
        return "Flush"
    
    cards = hand.split(" ")

    hand_of_cards = []
    for card in cards:
        hand_of_cards.append(Card(card))

    unique_values = []
    for card in hand_of_cards:
        if card.value not in unique_values:
            unique_values.append(card.value)

    if len(unique_values) == 2:
        return "4 of a kind"

    raise Exception

