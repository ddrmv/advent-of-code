import pytest
from mylib.helper import read_input
from y23_d12_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_12_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_12.txt')

def test_part1(example_input, full_input):
    assert part1(example_input) == 21
    assert part1(full_input) == 7653
