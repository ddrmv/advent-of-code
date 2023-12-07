import pytest
from mylib.helper import read_input
from y23_d07_p2 import Hand, part2

@pytest.fixture
def example_input():
    return read_input('y23_07_e.txt')
    
@pytest.fixture
def full_input():
    return read_input('y23_07.txt')

def test_part2(example_input, full_input):
    assert part2(example_input) == 5905
    assert part2(full_input) == 252137472
