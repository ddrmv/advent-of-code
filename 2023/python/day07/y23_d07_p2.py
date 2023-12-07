from typing import List

FACES = 'J23456789TQKA'
HAND_TYPE = {'5k': 6, '4k': 5, 'fh': 4, '3k': 3, '2p': 2, '1p': 1, 'hc': 0}

class Card():
    def __init__(self, card):
        self.face = card

    def __str__(self):
        return self.face

    def __eq__(self, other):
        return self.face == other.face

    def __hash__(self):
        return hash(self.face)

    def __lt__(self, other):
        return FACES.find(self.face) < FACES.find(other.face)


class Hand():
    def __init__(self, cards: str, bet: int):
        self.cards: List[Card]
        self.cards = [Card(card) for card in cards]
        self.bet = bet
        self.rank = None
        self.set_rank()

    def set_rank(self):
        card_set = set(self.cards)
        card_counts = [(card, self.cards.count(card)) for card in card_set]
        card_counts.sort(key=lambda c: c[1], reverse=True)
        unique_cards = len(card_counts)
        if card_counts[0][1] == 5:
            self.rank = HAND_TYPE['5k']
        elif card_counts[0][1] == 4:
            self.rank = HAND_TYPE['4k']
        elif card_counts[0][1] == 3 and unique_cards == 2:
            self.rank = HAND_TYPE['fh']
        elif card_counts[0][1] == 3:
            self.rank = HAND_TYPE['3k']
        elif card_counts[0][1] == 2 and card_counts[1][1] == 2:
            self.rank = HAND_TYPE['2p']
        elif card_counts[0][1] == 2 and unique_cards == 4:
            self.rank = HAND_TYPE['1p']
        elif unique_cards == 5:
            self.rank = HAND_TYPE['hc']
        else:
            raise ValueError
        
        js = self.cards.count(Card('J'))
        if js:
            self.adjust_for_js(js)

    def adjust_for_js(self, js):
        match js:
            case 4:
                self.rank = HAND_TYPE['5k']
            case 3:
                if self.rank == HAND_TYPE['fh']:
                    self.rank = HAND_TYPE['5k']
                elif self.rank == HAND_TYPE['3k']:
                    self.rank = HAND_TYPE['4k']
                else:
                    raise ValueError
            case 2:
                if self.rank == HAND_TYPE['fh']:
                    self.rank = HAND_TYPE['5k']
                elif self.rank == HAND_TYPE['3k']:
                    self.rank = HAND_TYPE['5k']
                elif self.rank == HAND_TYPE['2p']:
                    self.rank = HAND_TYPE['4k']
                elif self.rank == HAND_TYPE['1p']:
                    self.rank = HAND_TYPE['3k']
                else:
                    raise ValueError
            case 1:
                if self.rank == HAND_TYPE['4k']:
                    self.rank += 1
                elif self.rank == HAND_TYPE['fh'] or self.rank == HAND_TYPE['3k']:
                    self.rank = HAND_TYPE['4k']
                elif self.rank == HAND_TYPE['2p']:
                    self.rank = HAND_TYPE['fh']
                elif self.rank == HAND_TYPE['1p']:
                    self.rank = HAND_TYPE['3k']
                elif self.rank == HAND_TYPE['hc']:
                    self.rank = HAND_TYPE['1p']
                else:
                    raise ValueError
            case _:
                pass

    def __str__(self):
        return f"{''.join(str(card) for card in self.cards)},{self.rank},{self.bet}"
    
    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        elif self.rank == other.rank:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card < other_card:
                    return True
                elif self_card == other_card:
                    continue
                else:
                    return False
        return False


def part2(input):
    input_list = [line.split(' ') for line in input.rstrip().split('\n')]
    hands = [Hand(line[0], int(line[1])) for line in input_list]
    hands.sort()
    return sum((hand.bet * (index + 1)) for index, hand in enumerate(hands))
