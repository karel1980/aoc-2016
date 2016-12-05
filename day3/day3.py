
tuples = [ tuple([int(n) for n in x.split()]) for x in open('input').readlines() ]

def valid_triangle(tup):
	a,b,c = tup
	return (a+b > c) and (a+c > b) and (b+c > a)

print len(filter(valid_triangle, tuples))

from itertools import chain, product

helper = product(range(0, len(tuples), 3), range(3))
tuples2 = [ (tuples[row][col], tuples[row+1][col], tuples[row+2][col]) for row,col in helper ]

print len(filter(valid_triangle, tuples2))
