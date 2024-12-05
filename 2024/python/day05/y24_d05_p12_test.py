import pytest
from mylib.helper import read_input
from y24_d05_p12 import part1, part2
@pytest.fixture
def example_input():
    return read_input('y24_05_e.txt')

@pytest.fixture
def full_input():
    return read_input('y24_05.txt')

def test_part1(example_input):
    assert part1(example_input) == 143

def test_part1_full(full_input):
    assert part1(full_input) == 6051

def test_part2(example_input):
    assert part2(example_input) == 123

def test_part2_full(full_input):
    assert part2(full_input) == 5093
