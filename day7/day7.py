import re

def get_subnets(address):
    parts = re.findall("[a-z]+", address)
    for h in get_hypernets(address):
        parts.remove(h)
    return parts

def get_hypernets(address):
        return re.findall("\\[([^\\]]*)\\]", address)

def get_abas(nets):
    result = []
    for net in nets:
        for i in range(len(net)-2):
            xyz = net[i:i+3]
            if xyz[0] == xyz[2] and xyz[0] != xyz[1]:
                result.append(xyz)
    return result

def has_ssl(address):
    hypernets = get_hypernets(address)
    subnets = get_subnets(address)

    print "hhh", hypernets
    print "sss", subnets

    abas = get_abas(subnets)
    babs = get_abas(hypernets)

    print "abas", abas
    print "babs", babs

    for aba in abas:
        bab = aba[1] + aba[0] + aba[1]
        if bab in babs:
            return True

    return False

def day7_part2():
    lines = open('input').readlines()
    c = 0
    for address in lines:
        if has_ssl(address.strip()):
            c+=1

    return c

def run_tests():
    sut = "xyx[xyx]xyx"
    print get_subnets(sut)
    print get_hypernets(sut)
    print get_abas(get_subnets(sut))
    assert has_ssl("aba[bab]xyz") == True
    assert has_ssl("xyx[xyx]xyx") == False
    assert has_ssl("aaa[kek]eke") == True
    assert has_ssl("zazbz[bzb]cdb") == True

if __name__=="__main__":
    #run_tests()
    print day7_part2()
