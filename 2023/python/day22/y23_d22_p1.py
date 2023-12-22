class Brick():
    def __init__(self, x1, y1, z1, x2, y2, z2):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def __str__(self) -> str:
        return f'{self.x1},{self.y1},{self.z1}~{self.x2},{self.y2},{self.z2}'
    
    def __eq__(self, oth):
        if oth is None:
            return False
        return (self.x1 == oth.x1 and self.y1 == oth.y1 and self.z1 == oth.z1
                and self.x2 == oth.x2 and self.y2 == oth.y2 and self.z2 == oth.z2)


class Tower():
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.grid: list[list[list[int]]]
        self.bricks: list[Brick]
        self.bottoms_at_floor: dict[int, Brick]
        self.tops_at_floor: dict[int, Brick]
        self.grid = [[[None for z in range(z)] for y in range(y)] for x in range(x)]
        self.bricks = []

    def __str__(self) -> str:
        total = ''
        for floor in range(self.z):
            floor_string = ''
            for x in range(self.x):
                for y in range(self.y):
                    if self.grid[x][y][floor] == None:
                        floor_string += '.'
                    elif type(self.grid[x][y][floor]) == Brick:
                        floor_string += 'b'
                    else:
                        floor_string += self.grid[x][y][floor]
                floor_string += '\n'
            total += floor_string + '\n'
        return total

    def fill_brick_volume(self, b: Brick, fill: Brick | str):
        for x in range(b.x2 - b.x1 + 1):
            self.grid[b.x1 + x][b.y1][b.z1] = fill
        for y in range(b.y2 - b.y1 + 1):
            self.grid[b.x1][b.y1 + y][b.z1] = fill
        for z in range(b.z2 - b.z1 + 1):
            self.grid[b.x1][b.y1][b.z1 + z] = fill

    def fill_tower_with_bricks(self):
        # floor 0 (ground)
        for x in range(self.x):
            for y in range(self.y):
                self.grid[x][y][0] = '-'
        for b in self.bricks:
            self.fill_brick_volume(b, b)

    def can_move_down(self, b: Brick):
        floors = 0
        while True:
            if any(self.grid[b.x1 + x][b.y1][b.z1 - 1 - floors] != None for x in range(b.x2 - b.x1 + 1)):
                break
            if any(self.grid[b.x1][b.y1 + y][b.z1 - 1 - floors] != None for y in range(b.y2 - b.y1 + 1)):
                break
            floors += 1
        return floors

    def move_brick_down(self, b: Brick):
        steps = self.can_move_down(b)
        if steps > 0:
            self.fill_brick_volume(b, None)
            b.z1 -= steps
            b.z2 -= steps
            self.fill_brick_volume(b, b)
            return True
        return False

    def move_bricks_down(self):
        bricks_move = 0
        for brick in self.bricks:
            if self.move_brick_down(brick):
                bricks_move += 1
        return bricks_move
            

    def get_bricks_above(self, b: Brick):
        bricks_above = []
        for x in range(b.x2 - b.x1 + 1):
            high_brick = self.grid[b.x1 + x][b.y1][b.z2 + 1]
            if high_brick != None and high_brick not in bricks_above:
                bricks_above.append(high_brick)
        for y in range(b.y2 - b.y1 + 1):
            high_brick = self.grid[b.x1][b.y1 + y][b.z2 + 1]
            if high_brick != None and high_brick not in bricks_above:
                bricks_above.append(high_brick)
        return bricks_above
    
    def get_bricks_below(self, b: Brick):
        bricks_below = []
        for x in range(b.x2 - b.x1 + 1):
            high_brick = self.grid[b.x1 + x][b.y1][b.z1 - 1]
            if high_brick != None and high_brick not in bricks_below:
                bricks_below.append(high_brick)
        for y in range(b.y2 - b.y1 + 1):
            high_brick = self.grid[b.x1][b.y1 + y][b.z1 - 1]
            if high_brick != None and high_brick not in bricks_below:
                bricks_below.append(high_brick)
        return bricks_below

    def can_be_disintegrated(self, b: Brick):
        # see if this is the only brick under a brick above it
        bricks_above = self.get_bricks_above(b)
        for br in bricks_above:
            if len(self.get_bricks_below(br)) == 1:
                return False
        return True


def process_input(input: str) -> (list[Brick], Tower):
    bricks = []
    for line in input.rstrip().split('\n'):
        x1, y1, z1, x2, y2, z2 = tuple(int(n) for n in line.replace('~', ',').split(','))
        bricks.append(Brick(x1, y1, z1, x2, y2, z2))
    
    x_max = max(b.x2 for b in bricks) + 1
    y_max = max(b.y2 for b in bricks) + 1
    z_max = max(b.z2 for b in bricks) + 1
    tower = Tower(x_max, y_max, z_max)

    return bricks, tower


def part1(input):
    bricks: list
    tower: Tower
    bricks, tower = process_input(input)
    tower.bricks = bricks
    tower.fill_tower_with_bricks()
    bricks_move = 1
    while bricks_move:
        bricks_move = tower.move_bricks_down()
    return [tower.can_be_disintegrated(b) for b in tower.bricks].count(True)