import re

NODE_PATTERN = re.compile(".*x(\\d+)-y(\\d+)")

def is_viable(grid, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return False

    if grid[x1][y1][0] == 0:
        return False

    return grid[x1][y1][0] <= grid[x2][y2][1]

def get_grid(path):

    max_row = 0
    max_col = 0

    for l in open(path).readlines():
        parts = l.strip().split()

        m = NODE_PATTERN.match(parts[0])
        coords = (int(m.group(1)), int(m.group(2)))

        if coords[0] > max_col:
            max_col = coords[0]

        if coords[1] > max_row:
            max_row = coords[1]

    rows = max_row+1
    cols = max_col+1
    grid = [ [None for y in range(rows)] for x in range(cols) ]

    for l in open(path).readlines():
        parts = l.strip().split()

        m = NODE_PATTERN.match(parts[0])
        coords = (int(m.group(1)), int(m.group(2)))

        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])

        grid[coords[0]][coords[1]] = (used, avail)

    return grid

def show_grid(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print grid[x][y],
        print
    print

def get_viable(grid):
    viable = []

    nodes = []
    
    height = len(grid[1])
    width = len(grid)

    for x1 in range(width):
        for y1 in range(height):
            for x2 in range(width):
                for y2 in range(height):
                    if is_viable(grid, x1, y1, x2, y2):
                        viable.append([x1,y1,x2,y2])

    return viable

def get_viable_neighbours(grid):
    viable = []

    nodes = []
    
    height = len(grid[1])
    width = len(grid)

    for x1 in range(width):
        for y1 in range(height):
            neighbours = [(x1-1,y1), (x1+1,y1), (x1,y1-1), (x1,y1+1)]
            for x2,y2 in neighbours:
                if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height:
                    if is_viable(grid, x1, y1, x2, y2):
                        viable.append([x1,y1,x2,y2])

    return viable

def get_viable_count(grid):
    return len(get_viable(grid))

def samples():
    #print False, is_viable((0,0,0,1), (0,0,0,1))
    #print False, is_viable((0,0,0,1), (0,1,0,1))
    #print True, is_viable((0,0,1,1), (0,1,0,1))
    grid = get_grid('input')
    show_grid(grid)

    print get_viable_neighbours(grid)
    moves = ['l'] * 5
    moves += ['u'] * 34
    moves += ['r'] * 6

    moves += ['d','l','l','u','r'] * 28
    pos = (28,34)
    for l in moves:

        if l == 'u':
            pos = safe_move(grid, pos[0],pos[1]-1, pos[0],pos[1])
        if l == 'd':
            pos = safe_move(grid, pos[0],pos[1]+1, pos[0],pos[1])
        if l == 'l':
            pos = safe_move(grid, pos[0]-1,pos[1], pos[0],pos[1])
        if l == 'r':
            pos = safe_move(grid, pos[0]+1,pos[1], pos[0],pos[1])
        show_grid(grid)


    print get_viable_neighbours(grid)

    show_grid(grid)
    print len(moves)

def up(grid, x1, y1):
    return safe_move(grid, x1, y1, x1, y1-1)

def down(grid, x1, y1):
    return safe_move(grid, x1, y1, x1, y1+1)

def left(grid, x1, y1):
    return safe_move(grid, x1, y1, x1-1, y1)

def right(grid, x1, y1):
    return safe_move(grid, x1, y1, x1+1, y1)

def safe_move(grid, x1, y1, x2, y2):
    width = len(grid)
    height = len(grid[0])
    if x1 < 0 or x1 >= width or y1 < 0 or y1 >= height:
        raise Exception('not viable')
        print "not viable"
        return (x2,y2)
    if not is_viable(grid, x1, y1, x2, y2):
        raise Exception('not viable')
        print "Not viable"
        return (x2,y2)
    move(grid, x1, y1, x2, y2)

    return (x1, y1)

def move(grid, x1, y1, x2, y2):
    amount = grid[x1][y1][0]
    grid[x1][y1] = (0, grid[x1][y1][1] + amount)
    grid[x2][y2] = (grid[x2][y2][0] + amount, grid[x2][y2][1] - amount)

def day21_part1():
    print get_viable_count(get_grid('input'))

def day21_part2():
    print solve('another')

if __name__=="__main__":
    samples()
    #day21_part1()
    #day21_part2()
