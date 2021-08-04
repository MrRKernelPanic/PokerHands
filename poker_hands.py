from card import Card
from hand import Hand


def check_hand(raw_hand):    
    hand = Hand(raw_hand)
   
    return hand.find_poker_hand()

    raise Exception
