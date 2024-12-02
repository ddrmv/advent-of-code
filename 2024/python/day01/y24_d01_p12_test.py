import pytest
from mylib.helper import read_input
from y24_d01_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_01_e.txt')

@pytest.fixture
def full_input():
    return read_input('y24_01.txt')

def test_part1(example_input):
    assert part1(example_input) == 11

def test_part1_full(full_input):
    assert part1(full_input) == 2285373

def test_part2(example_input):
    assert part2(example_input) == 31

def test_part2_full(full_input):
    assert part2(full_input) == 21142653
