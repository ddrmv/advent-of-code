import pytest
import os
from part1_d4 import is_full_overlap, full_overlaps

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
    
def test_is_full_overlap():
    assert is_full_overlap("2-8,3-7") == True
    assert is_full_overlap("2-4,6-8") == False

def test_full_overlaps(example_input, full_input):
    assert full_overlaps(example_input) == 2
    assert full_overlaps(full_input) == 599