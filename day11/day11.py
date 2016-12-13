import itertools

def combination_allowed(items):
    generators = set([ i[0] for i in items if i[1] == "G" ])
    chips = set([ i[0] for i in items if i[1] == "M" ])

    if len(generators) == 0:
        return True

    unprotected = chips.difference(generators)
    if len(unprotected) > 0:
        return False

    return True

def bfs(initial):
    q = [ (0, initial) ]

    known_states = set()

    num_moves = 0
    while len(q) > 0:
        current = q.pop(0)

        depth, state = current

        if depth > num_moves:
            num_moves = depth
            print depth

        hashablestate = "%s %s"%(state[0], "#".join([ "".join(sorted(s)) for s in state[1]]))
        if hashablestate in known_states:
            continue

        known_states.add(hashablestate)

        pos, floors = state

        if len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2])==0:
            print "YAY", depth
            exit (0)

        items = floors[pos]
        combos = [ (i,) for i in items ]
        combos.extend([ combo for combo in itertools.combinations(items, 2)])
        # there can be invalid combos but they are filtered out when evaluating newfloor

        dirs = []
        if pos < 3:
            dirs.append(1)
        if pos > 0:
            dirs.append(-1)

        for d in dirs:
            for c in combos:
                newfloors = [ f for f in floors ]
                old_floor = floors[pos].difference(set(c))
                new_floor = floors[pos+d].union(set(c))

                if combination_allowed(old_floor) and combination_allowed(new_floor):
                    newfloors[pos] = old_floor
                    newfloors[pos+d] = new_floor

                    q.append((depth + 1, (pos+d, newfloors)))

def test():
    bfs((0, [set(["HM","LM"]), set(["HG"]), set(["LG"]), set([])]))

def day11_part1():
    bfs((0, [set(["SG","SM","PG","PM"]), set(["TG","RG","RM","CG","CM"]), set(["TM"]), set()]))

def day11_part2():
    bfs((0, [set(["EG", "EM", "DG", "DM", "SG","SM","PG","PM"]), set(["TG","RG","RM","CG","CM"]), set(["TM"]), set()]))

if __name__=="__main__":
    #test()
    #day11_part1()
    day11_part2()
