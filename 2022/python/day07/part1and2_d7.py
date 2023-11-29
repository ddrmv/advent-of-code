class Node:
    def __init__(self, name, is_dir, size=0):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_size(self):
        if self.is_dir:
            dir_size = 0
            for child in self.children:
                dir_size += child.get_size()
            return dir_size
        else:
            return self.size
    
    def smaller_than_100000(self):
        dir_size_sum = 0
        if self.is_dir:
            for child in self.children:
                if child.is_dir and child.get_size() <= 100000:
                    dir_size_sum += child.get_size() + child.smaller_than_100000()
                else:
                    dir_size_sum += child.smaller_than_100000()
        return dir_size_sum
    
    def get_sizes(self, sizes):
        if self.is_dir:
            sizes.append(self.get_size())
            for child in self.children:
                child.get_sizes(sizes)
        return sizes
    

class Tree:
    def __init__(self):
        self.root = Node("/", True)
        self.current = self.root

    def go_to_root(self):
        self.current = self.root
    
    def add_child(self, child):
        self.current.add_child(child)

    def go_up(self):
        self.current = self.current.parent

    def go_to_child(self, name):
        self.current = list(filter(lambda child: child.name == name, self.current.children))[0]


def parse_input(input):
    for line in input.rstrip().split("\n"):
        if line == '$ cd /':
            tree = Tree()
        elif line.startswith("$ cd .."):
            tree.go_up()
        elif line.startswith("$ cd"):
            tree.go_to_child(line[5:])
        elif line.startswith("dir"):
            tree.add_child(Node(line[4:], True))
        elif line.startswith("$ ls"):
            continue
        else:
            size = int(line.split(" ")[0])
            name = line.split(" ")[1]
            tree.add_child(Node(name, False, size))
    return tree

def part1(input):
    tree = parse_input(input)
    return tree.root.smaller_than_100000()

def part2(input):
    tree = parse_input(input)
    update_space, total_capacity = 30_000_000, 70_000_000
    necessary_space = update_space - (total_capacity - tree.root.get_size())
    dir_sizes = []
    tree.root.get_sizes(dir_sizes)
    dir_sizes.append(necessary_space)
    dir_sizes.sort()
    return dir_sizes[dir_sizes.index(necessary_space)+1]