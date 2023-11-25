import pytest
import os
from part1_d5 import process_moves

@pytest.fixture
def example_input():
    return '''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day05')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_process_moves(example_input, full_input):
    assert process_moves(example_input) == "CMZ"
    assert process_moves(full_input) == "VQZNJMWTR"