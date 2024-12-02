import os

def read_input(filename):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, f'../../../input/{filename}')
    with open(filename) as file:
        input = file.read()
        return input