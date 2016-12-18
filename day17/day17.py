import md5

def solve(passcode, part2 = False):
    initial = (0,0,passcode)
    q = [initial]
    directions = ["U","D","L","R"]

    longest = None

    while len(q) > 0:
        current = q.pop(0)
        x,y,code = current

        if x == 3 and y == 3:
            if part2:
                longest = len(code)-len(passcode)
                continue
            else:
                return code[len(passcode):]

        doors = list(md5.new(code).hexdigest()[:4])

        door_states = get_doorstates(doors)

        for direction in directions:
            dx,dy = get_movedirs(direction)

            if door_states[direction]: # True means open
                if x+dx >= 0 and y+dy >= 0 and x+dx < 4 and y+dy < 4:
                    q.append((x+dx, y+dy, code+direction))

    return longest
        
def get_doorstates(doors):
    open_states =  ['b','c','d','e','f']
    result = {}
    result["U"] = doors[0] in open_states
    result["D"] = doors[1] in open_states
    result["L"] = doors[2] in open_states
    result["R"] = doors[3] in open_states
    return result

def get_movedirs(letter):
    if letter == "U":
        return (0,-1)

    if letter == "D":
        return (0, 1)

    if letter == "L":
        return (-1, 0)

    if letter == "R":
        return (1, 0)

def sample():
    print "samples part1"
    print solve("ihgpwlah")
    print solve("kglvqrro")
    print solve("ulqzkmiv")

    print "samples part2"
    print solve("ihgpwlah", True)
    print solve("kglvqrro", True)
    print solve("ulqzkmiv", True)

def day17_part1():
    print solve("gdjjyniy")

def day17_part2():
    print solve("gdjjyniy", True)

if __name__=="__main__":
    #sample()
    day17_part1()
    day17_part2()
