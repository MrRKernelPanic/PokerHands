class Card:
    def __init__(self, raw_card):
        self.suit = raw_card[-1]
        self.value = raw_card.replace(self.suit,"")
        
        #if len(raw_card) == 2:
        #    self.value = raw_card[0]
        #    self.suit = raw_card[1]
        #else:
        #    self.value = raw_card[0:1]
        #    self.suit = raw_card[2]
