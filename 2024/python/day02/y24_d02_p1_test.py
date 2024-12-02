import pytest
from mylib.helper import read_input
from y24_d02_p1 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_02_e.txt')

@pytest.fixture
def full_input():
    return read_input('y24_02.txt')

def test_part1(example_input):
    assert part1(example_input) == 2

def test_part1_full(full_input):
    assert part1(full_input) == 383

def test_part2(example_input):
    assert part2(example_input) == 4

def test_part2_full(full_input):
    assert part2(full_input) == 436
