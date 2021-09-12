class Card:
    def __init__(self, raw_card):

        card_num_value = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
            }
        self.suit = raw_card[-1]
        raw_card_value = raw_card.replace(self.suit, "")

        if raw_card_value in card_num_value.keys():
            self.value = card_num_value[raw_card_value]
        else:
            self.value = int(raw_card_value)
