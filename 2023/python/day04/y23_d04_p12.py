from typing import List

class Card():
    def __init__(self, your_nums: List[int], win_nums: List[int], copies: int):
        self.your_nums = your_nums
        self.win_nums = win_nums
        self.copies = copies

    def get_hits_num(self):
        return len(set(self.your_nums).intersection(set(self.win_nums)))
        

def process_input(input):
    cards = []
    for card in input.rstrip().split("\n"):
        your_nums_part, win_nums_part = card.split(': ')[1].split(' | ')
        your_nums = [int(num) for num in your_nums_part.split(' ') if num.isdigit()]
        win_nums = [int(num) for num in win_nums_part.split(' ') if num.isdigit()]
        copies = 1
        cards.append(Card(your_nums, win_nums, copies))
    return cards

def find_number_of_hits(card: Card):
    return len(set(card.your_nums).intersection(set(card.win_nums)))

def hits_to_value(hits):
    return hits if hits < 2 else 2**(hits - 1)

def update_card_numbers(cards: List[Card]):
    for index, card in enumerate(cards):
        hits = card.get_hits_num()
        if hits != 0:
            for next_card_num in range(index + 1, index + 1 + hits):
                if next_card_num < len(cards):
                    cards[next_card_num].copies += card.copies
    
def get_total_number_of_cards(cards: List[Card]):
    return sum([card.copies for card in cards])


def part1(input):
    cards: List[Card] = process_input(input)
    return sum(hits_to_value(card.get_hits_num()) for card in cards)

def part2(input):
    cards = process_input(input)
    update_card_numbers(cards)
    return get_total_number_of_cards(cards)