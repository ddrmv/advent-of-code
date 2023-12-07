import pytest
from mylib.helper import read_input
from y23_d02_p2 import part2

@pytest.fixture
def example_input():
    return read_input('y23_02_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_02.txt')
    
def test_part2(example_input, full_input):
    assert part2(example_input) == 2286
    assert part2(full_input) == 65371