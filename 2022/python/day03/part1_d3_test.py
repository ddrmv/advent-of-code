import pytest
import os
from part1_d3 import backpack_score, item_value, total_score

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
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day03')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_item_value():
    assert item_value('a') == 1
    assert item_value('A') == 27

def test_backpack_score():
    assert backpack_score("vJrwpWtwJgWrhcsFMMfFFhFp") == 16

def test_total_score(example_input, full_input):
    assert total_score(example_input) == 157
    assert total_score(full_input) == 7908

