import pytest
from mylib.helper import read_input
from y23_d11_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_11_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_11.txt')

def test_part1(example_input, full_input):
    assert part1(example_input) == 374
    assert part1(full_input) == 9177603
