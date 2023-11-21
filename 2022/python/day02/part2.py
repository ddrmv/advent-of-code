def shape_needed(string):
    shape = {'A X': 'Z', 'B X': 'X', 'C X': 'Y',
            'A Y': 'X', 'B Y': 'Y', 'C Y': 'Z',
            'A Z': 'Y', 'B Z': 'Z', 'C Z': 'X'}
    return shape[string]

def outcome_score(string):
    score = {'X': 0, 'Y': 3, 'Z': 6}
    return score[string]

def shape_score(string):
    points = {'X': 1, 'Y': 2, 'Z': 3}
    return points[string]

def round_score(string):
    return shape_score(shape_needed(string)) + outcome_score(string[2])

def total_score(string):
    return sum(round_score(line) for line in string.strip().split('\n'))
