import md5
import re

def solve(salt):
    triples = []
    keys = 0
    index = 0

    while keys < 64:
        salted = "%s%s"%(salt,index)
        key = md5.new(salted).hexdigest()

        repeat3 = re.findall("(.)\\1\\1", key)
        repeat5 = re.findall("(.)\\1\\1\\1\\1", key)
        if len(repeat5) > 0:
            triples = filter(lambda t: t[0] >= index - 1000, triples)
            print triples
            #for r5 in repeat5:
            r5 = repeat5[0]
            for t in triples:
                if r5 == t[1]:
                    keys += 1
                    print index - t[0]
                    if keys >= 64:
                        return t[0]

        if len(repeat3) > 0:
            triples.append((index, repeat3[0]))

        index += 1

def md5hash(value):
    return md5.new(v).hexdigest()

def stretchhash(value):
    v = value

    for i in range(2017):
        v = md5.new(v).hexdigest()

    return v

def solve2(salt, hasher):
    repeat3 = []
    repeat5 = []

    keys = 0

    for i in range(50000):
        if i%1000 == 0: print i
        salted = "%s%s"%(salt,i)
        key = hasher(salted)

        r3 = re.findall("(.)\\1\\1", key)
        r5 = re.findall("(.)\\1\\1\\1\\1", key)

        if len(r3) > 0:
            repeat3.append((i, r3[0]))
        if len(r5) > 0:
            repeat5.append((i, r5[0]))

    r3idx = 0
    r5idx = 0
    print repeat5
    while keys < 64:
        r3 = repeat3[r3idx]
        r5 = repeat5[r5idx]
        print "at ", r3, r5

        while r3[0] >= r5[0]:
            print "r3 >= r5, increasing r5"
            r5idx += 1
            r5 = repeat5[r5idx]
            print r5

        if r3[0] + 1000 < r5[0]:
            print "r3 + 1000 < r5, increasing r3"
            r3idx+=1
            continue

        tmp = r5idx
        if repeat5[r5idx] == repeat3[r3idx]:
            tmp+=1
        print "checking for r5 withing 1000 of r3"
        while repeat5[tmp][0] <= r3[0] + 1000:
            if repeat5[tmp][1] == r3[1]:
                print "found one!", repeat5[tmp]
                keys+=1
                print keys
                if keys == 64:
                    return r3
                break
            tmp += 1

        r3idx += 1

def day14_part1():
    print solve2('ngcjuoqr', md5hash)

def day14_part2():
    print solve2('ngcjuoqr', stretchhash)

def sample():
    #print "yyy", solve2('abc')
    print stretchhash('abc0')

if __name__=="__main__":
    #sample()
    #day14_part1()
    day14_part2()

