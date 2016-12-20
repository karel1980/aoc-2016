from math import log, pow

def solve1_iter(n):
    elves = list(range(1, n+1))

    i = 1
    while len(elves) > 1:
        n += 1
        if (n%1000)== 0:
            print n
        elves.pop(i)
        i = (i+1)%len(elves)

    return elves[i]

def solve1_direct(n):
    a=log(n,2)
    b=int(log(n, 2))
    c = n - int(log(n, 2))
    c = n - (2**b)
    d = 1 + (2*c)
    return d

def remove_opposite_elf(elves, elf_idx):
    victim_idx = (elf_idx + int(len(elves) / 2))%len(elves)
    victim = elves.pop(victim_idx)

    if victim_idx > elf_idx:
        next_elf_idx = elf_idx + 1
    else:
        next_elf_idx = elf_idx

    if next_elf_idx == len(elves):
        next_elf_idx = 0

    return victim, next_elf_idx

def solve2_iter(n):
    elves = list(range(1, n+1))

    iterations = 0
    i = 0
    while len(elves) > 1:
        iterations += 1
        if iterations%1000 == 0:
            print iterations
        victim, i = remove_opposite_elf(elves, i)

    return elves

def examples():
    for n in range(3, 100):
        print n, solve1_iter(n), solve1_direct(n)

def examples2():
    n = 2
    for i in range(n):
        e = list(range(n))
        victim, next_elf  = remove_opposite_elf(e, i)
        print e,  next_elf
        print "elf %s stole from %s, next elf is %s"%(i,victim,e[next_elf])


def day19_part1():
    print solve1_direct(3018458)

def day19_part2():
    print solve2_iter(3018458)

if __name__=="__main__":
    #examples1()
    #day19_part1()

    #examples2()
    day19_part2()
