
def gendata(data, size):

    while len(data) < size:
        rev=data[::-1]
        rev = rev.replace("0", "x").replace("1", "0").replace("x", "1")

        data = data + "0" + rev

    data = data[:size]

    return data

def checksum(data):
    even = True
    while even:
        check = []
        for i in range(0, len(data)-1, 2):
            if data[i] != data[i+1] :
                check.append("0")
            else:
                check.append("1")

        data = "".join(check)
        print data
        even = len(data)%2 == 0

    print "checksum is",data
    return data

def solve(data, size):
    data = gendata(data, size)
    check = checksum(data)

def sample():
    #print gendata("1", 12)
    #print gendata("0", 12)
    #print gendata("11111", 12)
    #print checksum("110010110100"), " should be ", 100
    print solve("10000", 20)
    #print solve("110010110100", 12)

def day16_part1():
    print solve("10111100110001111", 272)

def day16_part2():
    print solve("10111100110001111", 35651584)

if __name__=="__main__":
    #sample()
    #day16_part1()
    day16_part2()
