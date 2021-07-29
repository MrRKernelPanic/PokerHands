class Card:
    def __init__(self, raw_card):
        self.value = raw_card[0]
        self.suit = raw_card[1]