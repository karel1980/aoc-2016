import re

def get_decompressed_length(line):
    print line
    pattern = re.compile("\\(\\d+x\\d+\\)")
    m = pattern.search(line)
    if m is None: return len(line)
    marker = m.group(0)
    pos = line.index(marker)
    while m != None:
        start = line[:pos]
        remainder = line[pos+len(marker):]

        length, repeat = marker[1:-1].split("x")
        length,repeat =int(length),int(repeat)
        to_expand = remainder[:length]
        expanded = to_expand*repeat

        line = start + expanded + remainder[length:]
        print "xxx", line
        remainder = remainder[length:]

        m = pattern.search(remainder)
        if m is not None:
            marker = m.group(0)
            pos = len(start) + len(expanded) + remainder.index(marker)

    return len(line)

def day9_part1():
    lines = open('input').readlines()

    line = lines[0].strip()

    return get_decompressed_length(line)

def recursive_decompress_length(line):
    pattern = re.compile("\\(\\d+x\\d+\\)")
    m = pattern.search(line)
    if m is None:
        return len(line)

    pos = line.index(m.group(0))
    length, repeat = m.group(0)[1:-1].split("x")
    length, repeat = int(length), int(repeat)

    group_decompressed = recursive_decompress_length(line[pos+len(m.group(0)):pos+len(m.group(0))+length])
    remainder_length = recursive_decompress_length(line[pos+len(m.group(0))+length:]) 

    return pos + repeat * group_decompressed + remainder_length

def day9_part2():
    lines = open('input').readlines()
    line = lines[0].strip()

    return recursive_decompress_length(line)

print day9_part2()

#print recursive_decompress_length("ADVENT")
#print recursive_decompress_length("A(1x5)BC")
#print recursive_decompress_length("(3x3)XYZ")
#print recursive_decompress_length("A(2x2)BCD(2x2)EFG")
#print recursive_decompress_length("(6x1)(1x3)A")
#print recursive_decompress_length("X(8x2)(3x3)ABCY")
