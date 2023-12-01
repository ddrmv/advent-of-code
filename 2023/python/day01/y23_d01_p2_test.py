import os, pytest
from y23_d01_p2 import find_first, find_last, part2

@pytest.fixture
def example_input():
    return '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day01')
    with open(filename) as file:
        full_input = file.read()
        return full_input
  
def test_find_first():
    assert find_first("abcone2threexyz") == "1"
    assert find_first("4nineeightseven2") == "4"

def test_find_last():
    assert find_last("abcone2threexyz") == "3"
    assert find_last("4nineeightseven2") == "2"

def test_part2(example_input, full_input):
    assert part2(example_input) == 281
    assert part2(full_input) == 56017