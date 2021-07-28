def check_hand(hand):
    hearts = hand.count("H")   
    spades = hand.count("S")
    clubs = hand.count("C")
    diamonds = hand.count("D")

    if hearts == 5 or spades == 5 or clubs == 5 or diamonds == 5:
        return "Flush"

    raise Exception
    