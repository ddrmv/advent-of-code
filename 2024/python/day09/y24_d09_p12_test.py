import pytest
from mylib.helper import read_input
from y24_d09_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_09_e.txt')

@pytest.fixture
def example_input_mini():
    return read_input('y24_09_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y24_09.txt')

def test_part1(example_input):
    assert part1(example_input) == 1928

def test_part1_mini(example_input_mini):
    assert part1(example_input_mini) == 60

def test_part1_full(full_input):
    assert part1(full_input) == 6337367222422

def test_part2(example_input):
    assert part2(example_input) == 2858

# pass in 0.57s
def test_part2_full(full_input):
    assert part2(full_input) == 6361380647183

