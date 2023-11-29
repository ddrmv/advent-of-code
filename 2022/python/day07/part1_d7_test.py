import pytest
import os
from part1_d7 import part1

@pytest.fixture
def example_input():
    return '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day07')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_part1(example_input, full_input):
    assert part1(example_input) == 95437
    assert part1(full_input) == 1792222