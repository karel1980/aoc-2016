#!/usr/bin/python

class Player:

	def __init__(self):
		self.x,self.y = 0,0
		self.dir = 0
		self.visited = set()
		self.doublevisit = None
		self.visited.add((0,0))

	def left(self):
		self.dir = (self.dir + 3)%4

	def right(self):
		self.dir = (self.dir + 1)%4

	def dx(self):
		if self.dir == 0:
			return 1
		if self.dir == 2:
			return -1
		return 0

	def dy(self):
		if self.dir == 1:
			return 1
		if self.dir == 3:
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

def main():
	lines = open('input').readlines()
	moves = [ m.strip() for m in ",".join(lines).split(",") ]

	p = Player()

	for m in moves:
		if m[0] == 'L':
			p.left()
		if m[0] == 'R':
			p.right()
		dist = int(m[1:])
		p.move(dist)
	
	print abs(p.x) + abs(p.y)

	print abs(p.doublevisit[0]) + abs(p.doublevisit[1])

if __name__=="__main__":
	main()
