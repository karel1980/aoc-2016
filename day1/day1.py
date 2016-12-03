#!/usr/bin/python

DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3

class Player:
	def __init__(self):
		self.x,self.y = 0,0
		self.dir = DIR_UP
		self.visited = set()
		self.doublevisit = None
		self.visited.add((0,0))

	def process_input_lines(self, lines):
		moves = [ m.strip() for m in ",".join(lines).split(",") ]
		for m in moves:
			if m[0] == 'L':
				self.left()
			if m[0] == 'R':
				self.right()
			dist = int(m[1:])
			self.move(dist)

	def left(self):
		self.dir = (self.dir + 3)%4

	def right(self):
		self.dir = (self.dir + 1)%4

	def dx(self):
		if self.dir == DIR_RIGHT:
			return 1
		if self.dir == DIR_LEFT:
			return -1
		return 0

	def dy(self):
		if self.dir == DIR_UP:
			return 1
		if self.dir == DIR_DOWN:
			return -1
		return 0

	def move(self, n):
		for i in range(1,n):
			nextpoint = (self.x+self.dx()*i,self.y+self.dy()*i)
			if self.doublevisit is None:
				if nextpoint in self.visited:
					self.doublevisit = nextpoint
			self.visited.add(nextpoint)

		self.x += self.dx()*n
		self.y += self.dy()*n

def day1_part1(filename):
	p = Player()
	p.process_input_lines(open(filename).readlines())
	return abs(p.x) + abs(p.y)

def day1_part2(filename):
	p = Player()
	p.process_input_lines(open(filename).readlines())
	return abs(p.doublevisit[0]) + abs(p.doublevisit[1])

def main():
	print day1_part1('input')
	print day1_part2('input')

if __name__=="__main__":
	main()
