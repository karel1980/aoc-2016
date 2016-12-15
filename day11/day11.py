import itertools

def remove_equivalent_pairs(items):
    generators = set([ i[0] for i in items if i[1] == "G"])
    chips = set([ i[0] for i in items if i[1] == "M" ])

    paired = chips.intersection(generators)

    if len(paired) > 0:
        items = set(items).difference([ p + "G" for p in paired ]).difference(set([ p + "M" for p in paired ]))
        p = list(paired)[0]
        return items.union([ p + "M", p + "G" ])

    return items
    
def combination_allowed(items):
    generators = set([ i[0] for i in items if i[1] == "G" ])
    chips = set([ i[0] for i in items if i[1] == "M" ])

    if len(generators) == 0:
        return True

    unprotected = chips.difference(generators)
    if len(unprotected) > 0:
        return False

    return True

def get_canonical_hashable_state(state):
    pos = state[0]
    floors = state[1]
    items_ordered = sorted(floors[0]) + sorted(floors[1]) + sorted(floors[2]) + sorted(floors[3])

    next_ord = 65
    mappings = {}
    for i in items_ordered:
        if i[0] in mappings:
            continue
        if i[0] not in mappings:
            mappings[i[0]] = chr(next_ord)
            next_ord += 1

    canon_floors = "#".join([ "".join(sorted(map(lambda item: mappings[item[0]] + item[1] , f))) for f in floors ])
    #canon_floors = "#".join([ "".join(sorted(f)) for f in floors ])
    return "%s %s"%(pos, canon_floors)

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

        hashablestate = get_canonical_hashable_state(state)
        if hashablestate in known_states:
            continue

        known_states.add(hashablestate)

        pos, floors = state

        if len(floors[0]) == 0 and len(floors[1]) == 0 and len(floors[2])==0:
            print "YAY", depth
            exit (0)

        items = remove_equivalent_pairs(floors[pos])
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
