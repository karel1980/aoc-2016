import re

def bfs_min_distance(grid, p1, p2):
    q = [(p1,0)]
    seen = set()

    while len(q)>0:
        p,d = q.pop(0)

        if p in seen:
            continue

        if p2 == p:
            return d

        seen.add(p)

        neighbours = grid.valid_neighbours(p)
        q.extend([(n,d+1) for n in neighbours])

    raise Exception('no path from %s to %s'%(p1,p2))

class Grid:
    def __init__(self, lines):
        self.lines = lines

        digit = re.compile('\\d')
        self.points = {}
        for y in range(len(lines)):
            line = lines[y]
            for x in range(len(line)):
                value = lines[y][x]
                if digit.match(value) != None:
                    self.points[lines[y][x]] = (x,y)

    def valid_neighbours(self, p):
        result = []

        x,y = p

        if x-1 >= 0 and self.lines[y][x-1] != '#':
                result.append((x-1,y))
        if x+1 < len(self.lines[0]) and self.lines[y][x+1] != '#':
                result.append((x+1,y))

        if y-1 >= 0 and self.lines[y-1][x] != '#':
                result.append((x,y-1))
        if y+1 < len(self.lines[0]) and self.lines[y+1][x] != '#':
                result.append((x,y+1))

        return result

    def show(self):
        for l in self.lines:
            print l,

def load_grid(path):
   return Grid(open(path).readlines()) 

def build_point_distance_graph(grid):
    result = {}
    
    for m1,p1  in grid.points.iteritems():
        links = []
        result[m1] = links

        for m2,p2 in grid.points.iteritems():
            links.append((m2, bfs_min_distance(grid, p1, p2)))

    return result

def depth_first_shortest_path(graph, current='0', visited=set(), distance = 0):
    print visited
    if len(graph) == len(visited):
        return distance

    best = 100000

    print "a add", current
    visited.add(current)
    for p, d in graph[current]:
        if p not in visited:
            #visited.add(p)
            #print "b add", p
            dist = depth_first_shortest_path(graph, p, visited, distance + d)
            if dist < best:
                best = dist
            #print "b remove", p
            #visited.remove(p)

    print "a remove", current
    visited.remove(current)

    if best == 100000: return distance
    return best

def samples():
    grid = load_grid('input')
    #grid.show()
    #print grid.points

    #print grid.valid_neighbours((1,1))

    #print bfs_min_distance(grid, grid.points['0'], grid.points['1'])

    graph = build_point_distance_graph(grid)
    #print graph
    print depth_first_shortest_path(graph, '0')

if __name__=="__main__":
    samples()


