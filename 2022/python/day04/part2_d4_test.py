import pytest
import os
from part2_d4 import any_overlaps

@pytest.fixture
def example_input():
    return '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day04')
    with open(filename) as file:
        full_input = file.read()
        return full_input
    
def test_any_overlaps(example_input, full_input):
    assert any_overlaps(example_input) == 4
    assert any_overlaps(full_input) == 928