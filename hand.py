from card import Card


class Hand:
    def __init__(self, raw_card_input):
        raw_cards_input = raw_card_input.split(" ")

        self.cards = []
        for card in raw_cards_input:
            self.cards.append(Card(card))
            