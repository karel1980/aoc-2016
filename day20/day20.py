
def in_range(low, high, value):
    return value >= low and value <= high

def overlaps(r1, r2):
    return in_range(r1[0], r1[1], r2[0]) or in_range(r1[0], r1[1], r2[1]) or r1[1]+1 == r2[0] or r2[1]+1 == r1[0]

def join(r1, r2):
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))

class Ranges:
    def __init__(self):
        self.ranges = []

    def add(self, low, high):
        overlapping = filter(lambda p: overlaps(p, (low,high)), self.ranges)
        self.ranges = filter(lambda p: not overlaps(p, (low,high)), self.ranges)

        if len(overlapping) > 0:
            to_add = (low,high)
            for other in overlapping:
               to_add = join(to_add, other)
        else:
            to_add = (low,high)

        self.ranges.append(to_add)

def get_ranges(path):
    ranges = Ranges()

    lines = open(path).readlines()

    lines = [ x.split("-") for x in lines ]
    lines = [ (int(a),int(b)) for a,b in lines ]

    for low, high in lines:
        ranges.add(low,high)

    ranges.ranges.sort()
    return ranges.ranges

def samples():
    #r = Ranges()
    #r.add(0,10)
    #r.add(11, 20)

    print solve('sample-input')

def day20_part1():
    print get_ranges('input')[0][1]+1

def day20_part2():
    ranges = get_ranges('input')
    num = 0
    for i in range(len(ranges)-1):
        num += ranges[i+1][0] - ranges[i][1] - 1

    MAX_VALUE=4294967295
    num += MAX_VALUE - ranges[-1][1]
    print num

if __name__=="__main__":
    #samples()
    #day20_part1()
    day20_part2()
