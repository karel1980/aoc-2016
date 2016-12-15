import math 
def generate_maze(designernr, size):
    maze = [ [False for i in range(size) ] for j in range(size) ]
    for x in range(size):
        for y in range(size):
            num = x*x + 3*x + 2*x*y + y + y*y
            num += designernr

            ones = bin(num).count("1")
            if ones %2 == 0:
                maze[y][x] = " "
            else:
                maze[y][x] = "#"

    return maze

def print_maze(maze):
    for row in maze:
        print "".join(row)

def test():
    print_maze(generate_maze(10))

def hdist(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def distance(start, target, maze):
    q = []

    size = len(maze)
    
    q.append((0, start))
    visited = set()
    
    while len(q) > 0:
        distance, pos = q.pop(0)
        if pos in visited:
            continue

        visited.add(pos)

        if pos == target:
            print "Found at distance ", distance
            return

        moves = []

        if pos[0] > 0:
            moves.append((pos[0]-1,pos[1]))
        if pos[0] < size-1:
            moves.append((pos[0]+1,pos[1]))
            
        if pos[1] > 0:
            moves.append((pos[0],pos[1]-1))
        if pos[1] < size-1:
            moves.append((pos[0],pos[1]+1))

        moves = filter(lambda m: maze[m[0]][m[1]]==" ", moves)
        moves.sort(cmp = lambda a,b: hdist(b,target)-hdist(a,target))

        for next_pos in moves:
            q.append((distance + 1, next_pos))

def reachable_count(start, maxdist, maze):
    q = []

    size = len(maze)
    
    q.append((0, start))
    visited = set()
    
    distance=0
    while len(q) > 0 and distance <= maxdist:
        distance, pos = q.pop(0)
        if pos in visited:
            continue

        visited.add(pos)
        maze[pos[0]][pos[1]] = "."

        moves = []

        if pos[0] > 0:
            moves.append((pos[0]-1,pos[1]))
        if pos[0] < size-1:
            moves.append((pos[0]+1,pos[1]))
            
        if pos[1] > 0:
            moves.append((pos[0],pos[1]-1))
        if pos[1] < size-1:
            moves.append((pos[0],pos[1]+1))

        moves = filter(lambda m: maze[m[0]][m[1]]!="#", moves)

        for next_pos in moves:
            q.append((distance + 1, next_pos))

    print len(visited)

def sample():
    col = 7
    row = 4
    maze = generate_maze(10, 10)
    print_maze(maze)

    distance((1,1), (row, col), maze)

def day13_part1():
    col = 31
    row = 39
    maze = generate_maze(1350, 1000)

    distance((1,1), (row, col), maze)

def day13_part2():
    maze = generate_maze(1350, 100)

    reachable_count((1,1), 50, maze)

if __name__=="__main__":
    #sample()
    #day13_part1()
    day13_part2()
