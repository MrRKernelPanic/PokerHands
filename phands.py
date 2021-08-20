from enum import Enum

class PHand(Enum):
    STRAIGHT_FLUSH = "Straight Flush"
    FOUR_OF_A_KIND ="4 of a kind"
    FULL_HOUSE = "Full house"
    FLUSH = "Flush"
    STRAIGHT = "Straight"
    THREE_UF_A_KIND = "3 of a kind"
    TWO_PAIRS = "2 pairs"
    A_PAIR = "a pair"
    HIGH_CARD = "the highest card"