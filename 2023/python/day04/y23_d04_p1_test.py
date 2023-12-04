import os, pytest
from y23_d04_p1 import process_input, hits_to_value, part1

@pytest.fixture
def example_input():
    return '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day04.txt')
    with open(filename) as file:
        full_input = file.read()
        return full_input

# def test_process_input(example_input):
#     assert process_input(example_input) == "a"

def test_hits_to_value():
    assert hits_to_value(0) == 0
    assert hits_to_value(1) == 1
    assert hits_to_value(2) == 2
    assert hits_to_value(3) == 4
    assert hits_to_value(4) == 8

def test_part1(example_input, full_input):
    assert part1(example_input) == 13
    assert part1(full_input) == 25004
