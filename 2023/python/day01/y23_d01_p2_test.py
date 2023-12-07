import pytest
from mylib.helper import read_input
from y23_d01_p2 import find_first, find_last, part2

@pytest.fixture
def example_input():
    return read_input('y23_01_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y23_01.txt')
  
def test_find_first():
    assert find_first("abcone2threexyz") == "1"
    assert find_first("4nineeightseven2") == "4"

def test_find_last():
    assert find_last("abcone2threexyz") == "3"
    assert find_last("4nineeightseven2") == "2"

def test_part2(example_input, full_input):
    assert part2(example_input) == 281
    assert part2(full_input) == 56017