import os, pytest
from y23_d06_p12 import part1, part2

@pytest.fixture
def example_input():
    return '''Time:      7  15   30
Distance:  9  40  200
'''
@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day06.txt')
    with open(filename) as file:
        full_input = file.read()
        return full_input


def test_part1(example_input, full_input):
    assert part1(example_input) == 288
    assert part1(full_input) == 588588

def test_part2(example_input, full_input):
    assert part2(example_input) == 71503
    assert part2(full_input) == 34655848
