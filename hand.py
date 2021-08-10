from card import Card


class Hand:
    def __init__(self, raw_card_input):
        raw_cards_input = raw_card_input.split(" ")
        self.max_card_num_value = 0
        self.min_card_num_value = 15
        self.unique_values = {}
        self.unique_suits = {}

        self.cards = []
        for card in raw_cards_input:
            self.cards.append(Card(card))

    def find_poker_hand(self):

        self.max_card_num_value = self.get_max_card_value()
        self.min_card_num_value = self.get_min_card_value()
        self.unique_values = self.get_unique_values()
        self.unique_suits = self.get_unique_suits()
        
        if len(self.unique_suits) == 1:
            if self.max_card_num_value - self.min_card_num_value == 4:
                return "Straight Flush"
            else:
                return "Flush"

        if self.max_card_num_value - self.min_card_num_value == 4:
            return "Straight"

        if self.unique_values[max(self.unique_values, key = self.unique_values.get)] == 4:
            return "4 of a kind"
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 3 and self.unique_values[min(self.unique_values, key=self.unique_values.get)] == 2:
            return "Full house"
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 3 and self.unique_values[min(self.unique_values, key=self.unique_values.get)] == 1:
            return "3 of a kind"
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 2:
            pair_count = 0
            for key in self.unique_values:
                if self.unique_values[key] == 2:
                    pair_count += 1
            
            if pair_count == 1:
                return "a pair"
            else:
                return "2 pairs"

    def get_unique_suits(self):
        for card in self.cards:
            if card.value not in self.unique_suits.keys():
                self.unique_suits[card.suit] = 1
            else:
                self.unique_suits[card.suit] += 1
        return self.unique_suits
    
    def get_unique_values(self):
        for card in self.cards:
            if card.value not in self.unique_values.keys():
                self.unique_values[card.value] = 1
            else:
                self.unique_values[card.value] += 1
        return self.unique_values
    
    def get_min_card_value(self):
        for card in self.cards:
            if card.value < self.min_card_num_value:
                self.min_card_num_value = card.value
        return self.min_card_num_value
    
    def get_max_card_value(self):
        for card in self.cards:
            if card.value > self.max_card_num_value:
                self.max_card_num_value = card.value
        return self.max_card_num_value
    