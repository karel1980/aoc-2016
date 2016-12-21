from day21 import swap_pos, move_pos_to_pos, get_instructions, swap_letters, rot_left, rot_right, rotate_letter_based, rev_move_pos_to_pos, rev_rotate_letter_based

base = "abcde"

def test_swap_pos():
    assert swap_pos(base, 1, 3)=="adcbe"
    assert swap_pos(base, 0, 1)=="bacde"
    assert swap_pos(base, 1, 0)=="bacde"

def test_swap_letters():
    assert swap_letters(base, 'b', 'd')=="adcbe"
    assert swap_letters(base, 'a', 'b')=="bacde"
    assert swap_letters(base, 'b', 'a')=="bacde"

def test_move_pos_to_pos():
    assert move_pos_to_pos(base, 1, 3)=="acdbe"

def test_rev_move_pos_to_pos():
    assert rev_move_pos_to_pos("acdbe", 1, 3)==base

def test_move_pos_to_pos_2():
    actual= move_pos_to_pos(base, 3, 1)
    assert actual=="adbce"

def test_rev_move_pos_to_pos_2():
    actual= rev_move_pos_to_pos("adbce", 3, 1)
    print actual
    assert actual==base

def test_rotate_left():
    assert rot_left(base, 0)=="abcde"
    assert rot_left(base, 1)=="bcdea"
    assert rot_left(base, 2)=="cdeab"
    assert rot_left(base, 3)=="deabc"
    assert rot_left(base, 4)=="eabcd"
    assert rot_left(base, 5)=="abcde"
    print rot_left(base, 6)
    assert rot_left(base, 6)=="bcdea"

def test_rotate_right():
    assert rot_right(base, 0)=="abcde"
    assert rot_right(base, 1)=="eabcd"
    assert rot_right(base, 2)=="deabc"
    assert rot_right(base, 3)=="cdeab"
    assert rot_right(base, 4)=="bcdea"
    assert rot_right(base, 5)=="abcde"
    assert rot_right(base, 6)=="eabcd"

def test_rotate_letter_based():
    assert rotate_letter_based(base, 'a')=="eabcd"
    assert rotate_letter_based(base, 'b')=="deabc"
    assert rotate_letter_based(base, 'c')=="cdeab"
    assert rotate_letter_based(base, 'd')=="bcdea"

def test_rev_rotate_letter_based():
    assert rev_rotate_letter_based("eabcd", 'a')==base
    assert rev_rotate_letter_based("deabc", 'b')==base
    assert rev_rotate_letter_based("cdeab", 'c')==base
    assert rev_rotate_letter_based("bcdea", 'd')==base

def test_samples():
    instructions = get_instructions('sample-input')
    word = "abcde"
    for i in instructions:
        print word
        word=i(word)
    print word
    assert word == "decab"
