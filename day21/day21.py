import re

def swap_pos(word, pos1, pos2):
    pos1,pos2 = min(pos1,pos2), max(pos1,pos2)
    a = word[pos1]
    b = word[pos2]
    return word[:pos1] + b + word[pos1+1:pos2] + a + word[pos2+1:]

def swap_letters(word, let1, let2):
    return swap_pos(word, word.index(let1), word.index(let2))

def rot_left(word, n):
    return word[n%len(word):] + word[:n%len(word)]

def rot_right(word, n):
    n = -n % len(word)
    return word[n:] + word[:n]

def reverse_substr(word, pos1, pos2):
    a = word[:pos1]
    b = word[pos1:pos2+1]
    c = word[pos2+1:]
    return a + b[::-1] + c

def rev_move_pos_to_pos(word, pos1, pos2):
    return move_pos_to_pos(word, pos2, pos1)


# abcde


def move_pos_to_pos(word, pos1, pos2):
    letter = word[pos1]

    if pos1 <= pos2:
        # a before letter
        # b letter
        # c after letter, before target pos
        # d after target pos
        a = word[:pos1]
        b = word[pos1]
        c = word[pos1+1:pos2+1]
        d = word[pos2+1:]

        return a + c + b + d
    if pos1 > pos2:
        #01234
        #abcde
        #a + d + bc + e
        a = word[:pos2]
        d = word[pos1]
        bc = word[pos2:pos1]
        e = word[pos1+1:]
        return a + d + bc + e

def rotate_letter_based(word, letter):
    num = word.index(letter)
    offset = 1 if num < 4 else 2
    return rot_right(word, (num + offset)%len(word))

def rev_rotate_letter_based(word, letter):
    for i in range(len(word)):
        w=rot_right(word,i)
        if rotate_letter_based(w, letter) == word:
            return w

def samples():
    word="abcde"

    word = swap_pos(word, 4, 0)
    print word == "ebcda"
    
    word = swap_letters(word, "b", "d")
    print word == "edcba"

    word = reverse_substr(word, 0 , 4)
    print word == "abcde"

    word = rot_left(word, 1)
    print word == "bcdea"

    word = move_pos_to_pos(word, 1, 4)
    print word == "bdeac"

    word = move_pos_to_pos(word, 3, 0)
    print word == "abdec"

    word = rotate_letter_based(word, "b")
    print word == "ecabd"

    word = rotate_letter_based(word, "d")
    print word == "decab"

    print 
    print rot_right("abcde", 0)
    print rot_right("abcde", 1)
    print rot_right("abcde", 2)
    print rot_right("abcde", 3)
    print rot_right("abcde", 4)
    print rot_right("abcde", 5)
    print rot_right("abcde", 6)

def get_instructions(path):
    result = []
    f = InstructionFactory()
    for line in open(path).readlines():
        result.append(f.create_instruction(line.strip()))
    return result

def get_instructions_reverse(path):
    result = []
    f = InstructionFactory()
    for line in open(path).readlines():
        result.append(f.create_instruction_reverse(line.strip()))
    return result

class InstructionFactory:
    def __init__(self):
        self.p1 = re.compile('move position (\\d) to position (\\d)')
        self.p2 = re.compile('reverse positions (\\d) through (\\d)')
        self.p3 = re.compile('rotate based on position of letter ([a-h])')
        self.p4 = re.compile('rotate left (\\d) steps?')
        self.p5 = re.compile('rotate right (\\d) steps?')
        self.p6 = re.compile('swap letter ([a-h]) with letter ([a-h])')
        self.p7 = re.compile('swap position (\\d) with position (\\d)')

    def create_instruction(self, line):
        m = self.p1.match(line)
        if m is not None:
            return lambda word: move_pos_to_pos(word, int(m.group(1)), int(m.group(2)))

        m = self.p2.match(line)
        if m is not None:
            return lambda word: reverse_substr(word, int(m.group(1)), int(m.group(2)))

        m = self.p3.match(line)
        if m is not None:
            return lambda word: rotate_letter_based(word, m.group(1))

        m = self.p4.match(line)
        if m is not None:
            return lambda word: rot_left(word, int(m.group(1)))

        m = self.p5.match(line)
        if m is not None:
            return lambda word: rot_right(word, int(m.group(1)))

        m = self.p6.match(line)
        if m is not None:
            return lambda word: swap_letters(word, m.group(1), m.group(2))

        m = self.p7.match(line)
        if m is not None:
            return lambda word: swap_pos(word, int(m.group(1)), int(m.group(2)))

    def create_instruction_reverse(self, line):
        m = self.p1.match(line)
        if m is not None:
            return lambda word: rev_move_pos_to_pos(word, int(m.group(1)), int(m.group(2)))

        m = self.p2.match(line)
        if m is not None:
            return lambda word: reverse_substr(word, int(m.group(1)), int(m.group(2)))

        m = self.p3.match(line)
        if m is not None:
            return lambda word: rev_rotate_letter_based(word, m.group(1))

        m = self.p4.match(line)
        if m is not None:
            return lambda word: rot_right(word, int(m.group(1)))

        m = self.p5.match(line)
        if m is not None:
            return lambda word: rot_left(word, int(m.group(1)))

        m = self.p6.match(line)
        if m is not None:
            return lambda word: swap_letters(word, m.group(1), m.group(2))

        m = self.p7.match(line)
        if m is not None:
            return lambda word: swap_pos(word, int(m.group(1)), int(m.group(2)))

        raise Exception(line)

def scramble(word, instructions):
    for i in instructions:
        word = i(word)

    return word

def unscramble(word, instructions):
    for i in reversed(instructions):
        word = i(word)

    return word

def day21_part1():
    instructions = get_instructions('input')
    word = "abcdefgh"
    print scramble(word, instructions)

def day21_part1_reversed():
    instructions = get_instructions_reverse('input')
    word = "gfdhebac"
    print unscramble(word, instructions)

def day21_part2():
    instructions = get_instructions_reverse('input')
    word = "fbgdceah"
    instructions.reverse()
    for i in instructions:
        word = i(word)

    print word

if __name__=="__main__":
    samples()
    day21_part1()
    day21_part1_reversed()
    day21_part2()


