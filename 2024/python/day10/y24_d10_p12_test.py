import pytest
from mylib.helper import read_input
from y24_d10_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_10_e.txt')

@pytest.fixture
def example_input_mini():
    return read_input('y24_10_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y24_10.txt')

def test_part1(example_input):
    assert part1(example_input) == 36

def test_part1_full(full_input):
    assert part1(full_input) == 816

def test_part2_mini(example_input_mini):
    assert part2(example_input_mini) == 3

def test_part2(example_input):
    assert part2(example_input) == 81

def test_part2_full(full_input):
    assert part2(full_input) == 1960
