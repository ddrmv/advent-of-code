import pytest
import os
from part2 import total_score

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

def test_total_score(example_input, full_input):
    assert total_score(example_input) == 12
    assert total_score(full_input) == 13889