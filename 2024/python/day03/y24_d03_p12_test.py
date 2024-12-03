import pytest
from mylib.helper import read_input
from y24_d03_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_03_e.txt')

@pytest.fixture
def example_input_2():
    return read_input('y24_03_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y24_03.txt')

def test_part1(example_input):
    assert part1(example_input) == 161

def test_part1_full(full_input):
    assert part1(full_input) == 173419328

def test_part2(example_input_2):
    assert part2(example_input_2) == 48

def test_part2_full(full_input):
    assert part2(full_input) == 90669332
