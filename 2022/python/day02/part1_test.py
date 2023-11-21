import pytest
import os
from part1 import outcome_score, shape_score, round_score, total_score

@pytest.fixture
def example_input():
    return '''A Y
B X
C Z
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day02')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_outcome_score():
    assert outcome_score('A Y') == 6
    assert outcome_score('A X') == 3
    assert outcome_score('C Y') == 0

def test_shape_score():
    assert shape_score('X') == 1
    assert shape_score('Y') == 2
    assert shape_score('Z') == 3

def test_round_score():
    assert round_score('A Y') == 8
    assert round_score('B X') == 1

def test_total_score(full_input, example_input):
    assert total_score(example_input) == 15
    assert total_score(full_input) == 14827