
def solve(row, count):
    row = [ True if t == "^" else False for t in row ]

    safe = count_safe(row)
    print_row(row)
    for i in range(1, count):
        row = next_row(row)
        safe += count_safe(row)

    return safe

def count_safe(row):
    return sum([0 if t else 1 for t in row])

def print_row(row):
    row = [ "." if t == False else "^" for t in row ]
    print "".join(row)

def next_row(row):

    row = [False] + row + [False]
    result = []

    for i in range(1, len(row)-1):
        a,b,c = row[i-1:i+2]

        result.append(a ^ c)

    return result

def sample():
    print solve("..^^.", 40)

def day18_part1():
    print solve(".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....", 40)

def day18_part2():
    print solve(".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^....", 400000)

if __name__ == "__main__":
    #sample()
    day18_part1()
    day18_part2()
