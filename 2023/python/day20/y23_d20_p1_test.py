import pytest
from mylib.helper import read_input
from y23_d20_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_20_e.txt')

@pytest.fixture
def example_input_2():
    return read_input('y23_20_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y23_20.txt')

def test_part1(example_input):
    assert part1(example_input) == 32000000

def test_part1_ex2(example_input_2):
    assert part1(example_input_2) == 11687500

def test_part1_full(full_input):
    assert part1(full_input) == 883726240