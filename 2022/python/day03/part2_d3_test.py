import pytest
import os
from part2_d3 import find_badge, total_badges

@pytest.fixture
def example_input():
    return '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

@pytest.fixture
def three_input():
    return ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg']

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day03')
    with open(filename) as file:
        full_input = file.read()
        return full_input
    
def test_find_badge(three_input):
    assert find_badge(three_input) == 'r'

def test_total_badges(example_input, full_input):
    assert total_badges(example_input) == 70
    assert total_badges(full_input) == 2838