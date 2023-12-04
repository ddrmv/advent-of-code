def process_input(input):
    cards = []
    for card in input.rstrip().split("\n"):
        your_numbers_part, winning_numbers_part = card.split(': ')[1].split(' | ')
        your_numbers = [int(num) for num in your_numbers_part.split(' ') if num.isdigit()]
        winning_numbers = [int(num) for num in winning_numbers_part.split(' ') if num.isdigit()]
        card_copies = 1
        cards.append([your_numbers, winning_numbers, card_copies])
    return cards

def find_number_of_hits(card):
    return len(set(card[0]).intersection(set(card[1])))

def hits_to_value(hits):
    return hits if hits < 2 else 2**(hits - 1)

def update_card_numbers(cards):
    for index, card in enumerate(cards):
        hits = find_number_of_hits(card)
        if hits != 0:
            for next_card_num in range(index + 1, index + 1 + hits):
                if next_card_num < len(cards):
                    cards[next_card_num][2] += card[2]
    
def get_total_number_of_cards(cards):
    return sum([card[2] for card in cards])

def part1(input):
    cards = process_input(input)
    return sum(hits_to_value(find_number_of_hits(card)) for card in cards)

def part2(input):
    cards = process_input(input)
    update_card_numbers(cards)
    return get_total_number_of_cards(cards)