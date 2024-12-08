import pytest
from mylib.helper import read_input
from y24_d08_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_08_e.txt')

@pytest.fixture
def example_input_mini():
    return read_input('y24_08_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y24_08.txt')

def test_part1(example_input):
    assert part1(example_input) == 14

def test_part1_full(full_input):
    assert part1(full_input) == 247

def test_part2_mini(example_input_mini):
    assert part2(example_input_mini) == 15

def test_part2(example_input):
    assert part2(example_input) == 34

def test_part2_full(full_input):
    assert part2(full_input) == 861
