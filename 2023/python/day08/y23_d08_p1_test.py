import pytest
from mylib.helper import read_input
from y23_d08_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_08_e.txt')
    
@pytest.fixture
def example_input_2():
    return read_input('y23_08_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y23_08.txt')

def test_part1(example_input, example_input_2, full_input):
    assert part1(example_input) == 2
    assert part1(example_input_2) == 6
    assert part1(full_input) == 12083
