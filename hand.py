from card import Card
from phands import PHand

class Hand:

    dict_high_card_lookup = {
        PHand.STRAIGHT_FLUSH.value : 1, 
        PHand.FOUR_OF_A_KIND.value : 4,
        PHand.FULL_HOUSE.value : 3,
        PHand.FLUSH.value : 1,
        PHand.STRAIGHT.value : 1,
        PHand.THREE_UF_A_KIND.value :3,
        PHand.TWO_PAIRS.value : 2,
        PHand.A_PAIR.value : 2,
        PHand.HIGH_CARD.value : 1
        }  
        
    def __init__(self, raw_card_input, player_colour):
        raw_cards_input = raw_card_input.split(" ")
        self.max_card_num_value = 0
        self.min_card_num_value = 15
        self.unique_values = {}
        self.unique_suits = {}

        self.cards = []
        for card in raw_cards_input:
            self.cards.append(Card(card))

        self.card_values = []
        self.remainder_values = []
        self.phand = self.search_for_poker_hand()
        self.highest_card_in_tie_breaker = self.highest_card_for_tie_breaker(self.dict_high_card_lookup.get(self.phand))
        self.remainder_hand_after_high_hand = self.remainder_hand_after_highest_poker_hand()
        self.hand_colour = player_colour
        self.two_pair_last_card_value = self.two_pair_last_card()

    def find_poker_hand(self):
        return self.phand

    def search_for_poker_hand(self):
        self.max_card_num_value = self.get_max_card_value()
        self.min_card_num_value = self.get_min_card_value()
        self.unique_values = self.get_unique_values()
        self.unique_suits = self.get_unique_suits()
        self.card_values = self.get_card_values()

        if len(self.unique_suits) == 1:

            if self.max_card_num_value - self.min_card_num_value == 4:
                return PHand.STRAIGHT_FLUSH.value
            else:
                return PHand.FLUSH.value

        if self.max_card_num_value - self.min_card_num_value == 4 and self.unique_values[max(self.unique_values, key = self.unique_values.get)] == 1:
            return PHand.STRAIGHT.value

        if self.unique_values[max(self.unique_values, key = self.unique_values.get)] == 4:
            return PHand.FOUR_OF_A_KIND.value
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 3 and self.unique_values[min(self.unique_values, key=self.unique_values.get)] == 2:
            return PHand.FULL_HOUSE.value
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 3 and self.unique_values[min(self.unique_values, key=self.unique_values.get)] == 1:
            return PHand.THREE_UF_A_KIND.value
        elif self.unique_values[max(self.unique_values, key=self.unique_values.get)] == 2:
            pair_count = 0
            for key in self.unique_values:
                if self.unique_values[key] == 2:
                    pair_count += 1
            
            if pair_count == 1:
                return PHand.A_PAIR.value
            else:
                return PHand.TWO_PAIRS.value
        else:
            return PHand.HIGH_CARD.value
            
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
    
    def get_card_values(self):
        self.card_values=[]
        for card in self.cards:
            self.card_values.append(card.value)
        self.card_values.sort(reverse=True)
        return self.card_values

    def highest_card_for_tie_breaker(self, num_same_value_cards):
        high_card_value = 0
        for each_card in self.card_values:
            count = self.card_values.count(each_card)
            if count == num_same_value_cards:
                if each_card >= high_card_value:
                    high_card_value = each_card
        return high_card_value
    
    def remainder_hand_after_highest_poker_hand(self):
        self.remainder_values = self.card_values.copy()
        r_item = self.highest_card_in_tie_breaker
        while r_item in self.remainder_values: self.remainder_values.remove(r_item)
        unique_values={}
        for card in self.remainder_values:
            if card not in unique_values.keys():
                unique_values[card] = 1
            else:
                unique_values[card] += 1
        
        if unique_values[max(unique_values, key=unique_values.get)] == 2:
            self.highest_card_of_remaining_hand = self.remainder_high_card_after_high_hand(2)
            return PHand.A_PAIR.value        
        else:
            self.highest_card_of_remaining_hand = self.remainder_high_card_after_high_hand(1)
            return PHand.HIGH_CARD.value
    
    def remainder_high_card_after_high_hand(self, num_same_value_cards):
        high_card_value = 0
        for each_card in self.remainder_values:
            count = self.remainder_values.count(each_card)
            if count == num_same_value_cards:
                if each_card >= high_card_value:
                    high_card_value = each_card
        return high_card_value

    def two_pair_last_card(self):
        check_for_single_cards = []
        for each_card in self.card_values:
            if self.card_values.count(each_card) == 1:
                check_for_single_cards.append(each_card)
        
        if len(check_for_single_cards) == 1:
            return check_for_single_cards[0]
        return 0
