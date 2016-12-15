
def success_at(t, disks):
    i = 0
    for d in disks:
        i += 1
        if (t+i+(d[0]+d[1]))%d[0] != 0:
            return False

    return True


def solve(disks):
    t = 0
    while True:
        if success_at(t, disks):
            return t
        t += 1

def sample():
    disks = [(5,4), (2,1)]
    print solve(disks)
    
def day15_part1():
    disks = [(5,2),(13,7),(17,10),(3,2),(19,9), (7,0)]
    print solve(disks)

def day15_part2():
    disks = [(5,2),(13,7),(17,10),(3,2),(19,9), (7,0), (11,0)]
    print solve(disks)

if __name__=="__main__":
    sample()
    day15_part1()
    day15_part2()
