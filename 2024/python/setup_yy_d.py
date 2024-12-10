# This script creates template files for day 'd' of year 'yy' in current directory and input directory
# Use: "python setup_yy_d.py 24 7" to create the files for day 7 of year 2024
# The above command creates the following files, only if they do not exist yet:
# - day07/y24_d07_p12.py
# - day07/y24_d07_p12_test.py
# - ../../input/y24_07_e.txt
# - ../../input/y24_07.txt

import sys
import os

def create_day_file(year, day):

    directory = f"day{day:02d}"

    # Create test file
    path = f"{directory}/y{year % 100}_d{day:02d}_p12_test.py"
    os.makedirs(directory, exist_ok=True)

    if os.path.exists(path):
        print(f"File {path} already exists")
    else:

        file_content = f"""import pytest
from mylib.helper import read_input
from y{year:02}_d{day:02}_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y{year:02}_{day:02}_e.txt')

@pytest.fixture
def full_input():
    return read_input('y{year:02}_{day:02}.txt')

def test_part1(example_input):
    assert part1(example_input) == -1

# def test_part1_full(full_input):
#     assert part1(full_input) == -1

# def test_part2(example_input):
#     assert part2(example_input) == -1

# def test_part2_full(full_input):
#     assert part2(full_input) == -1
"""
        
        with open(path, "w") as f:
            f.write(file_content)

        print(f"File {path} created")


# Create main file
    path = f"{directory}/y{year % 100}_d{day:02d}_p12.py"
    os.makedirs(directory, exist_ok=True)

    if os.path.exists(path):
        print(f"File {path} already exists")
    else:

        file_content = f"""def process_input(input: str):
    return input


def part1(input):
    return 0


def part2(input):
    return 0
"""
        
        with open(path, "w") as f:
            f.write(file_content)

        print(f"File {path} created")



    # also create empty files for input in directory ../../../input
    input_dir = "../../input"
    os.makedirs(input_dir, exist_ok=True)
    for filename in [f"y{year % 100}_{day:02}_e.txt", f"y{year % 100}_{day:02}.txt"]:
        path = f"{input_dir}/{filename}"
        if os.path.exists(path):
            print(f"File {path} already exists")
            continue
        with open(path, "w") as f:
            f.write("")

        print(f"File {path} created")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python setup_day_x.py <year> <day>")
        sys.exit(1)
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    create_day_file(year, day)

