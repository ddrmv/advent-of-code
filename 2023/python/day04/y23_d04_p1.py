def process_input(input):
    cards = []
    for card in input.rstrip().split("\n"):
        card_num_part, numbers_part = card.split(': ')
        card_number = card_num_part.split(' ')[1]
        your_numbers_part, winning_numbers_part = numbers_part.split(' | ')
        your_numbers = [int(num) for num in your_numbers_part.split(' ') if num.isdigit()]
        winning_numbers = [int(num) for num in winning_numbers_part.split(' ') if num.isdigit()]
        cards.append([card_number, your_numbers, winning_numbers])
    return cards

def find_number_of_hits(card):
    return len(set(card[1]).intersection(set(card[2])))

def hits_to_value(hits):
    return hits if hits < 2 else 2**(hits - 1)

def part1(input):
    cards = process_input(input)
    return sum(hits_to_value(find_number_of_hits(card)) for card in cards)