import os, pytest
from y23_d03_p1 import part1, part2

@pytest.fixture
def example_input():
    return '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day03.txt')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_part1(example_input, full_input):
    assert part1(example_input) == 4361
    assert part1(full_input) == 536202

def test_part2(example_input, full_input):
    assert part2(example_input) == 467835
    assert part2(full_input) == 78272573