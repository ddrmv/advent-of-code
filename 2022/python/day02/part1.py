def outcome_score(string):
    points = {'A X': 3, 'B X': 0, 'C X': 6,
            'A Y': 6, 'B Y': 3, 'C Y': 0,
            'A Z': 0, 'B Z': 6, 'C Z': 3}
    return points[string]

def shape_score(string):
    points = {'X': 1, 'Y': 2, 'Z': 3}
    return points[string]

def round_score(string):
    return outcome_score(string) + shape_score(string[2])

def total_score(string):
    return sum(round_score(line) for line in string.strip().split('\n'))
