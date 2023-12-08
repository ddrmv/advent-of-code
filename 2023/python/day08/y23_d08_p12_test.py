import pytest
from mylib.helper import read_input
from y23_d08_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_08_e.txt')
    
@pytest.fixture
def example_input_2():
    return read_input('y23_08_e2.txt')

@pytest.fixture
def example_input_3():
    return read_input('y23_08_e3.txt')

@pytest.fixture
def full_input():
    return read_input('y23_08.txt')

def test_part1(example_input, example_input_2, full_input):
    assert part1(example_input) == 2
    assert part1(example_input_2) == 6
    assert part1(full_input) == 12083

def test_part2(example_input_3, full_input):
    assert part2(example_input_3) == 6
    assert part2(full_input) == 13385272668829
    