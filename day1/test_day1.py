from day1 import Player

def test_moving_around_simple():
	lines=['R2, L3']

	p = Player()
	p.process_input_lines(lines)

	print p.x,p.y
	assert p.x == 2
	assert p.y == 3
