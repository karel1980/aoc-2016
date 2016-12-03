#!/bin/bash

class NumInput():
	def __init__(self):
		self.x, self.y = 1,1

	def left(self):
		self.x = max(0, self.x-1)
	def right(self):
		self.x = min(2, self.x+1)
	def up(self):
		self.y = max(0, self.y-1)
	def down(self):
		self.y = min(2, self.y+1)

	def number(self):
		return self.x+1 + self.y*3

class CrossInput():
	def __init__(self):
		self.pos = 0,2

		self.tiles = [ "..1..", ".234.", "56789", ".ABC.", "..D.." ]

	def go(self, dx, dy):
		x,y = self.pos[0]+dx,self.pos[1]+dy
		if self.allow_pos(x,y):
			self.pos = x,y

	def allow_pos(self,x,y):
		if y < 0 or y > 4:
			return False
		if x < 0 or x > 4:
			return False

		if self.tiles[y][x] == '.':
			return False

		return True

	def left(self):
		self.go(-1,0)
	def right(self):
		self.go(1,0)
	def up(self):
		self.go(0,-1)
	def down(self):
		self.go(0,1)

	def number(self):
		return self.tiles[self.pos[1]][self.pos[0]]

class Typist():
	def __init__(self, keyboard):
		self.keyboard = keyboard
		self.digits = []

	def process_input_lines(self, lines):
		for l in lines:
			for c in l:
				if c == 'U':
					self.keyboard.up()
				if c == 'D':
					self.keyboard.down()
				if c == 'L':
					self.keyboard.left()
				if c == 'R':
					self.keyboard.right()
			self.digits.append(self.keyboard.number())

def day2_part1(lines):
	t = Typist(NumInput())
	t.process_input_lines(lines)
	return t.digits
	
def day2_part2(lines):
	t = Typist(CrossInput())
	t.process_input_lines(lines)
	return t.digits
	
def main():
	lines = open('input').readlines()

	print day2_part1(lines)
	print day2_part2(lines)

if __name__ == '__main__':
	main()

