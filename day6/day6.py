lines = open('input').readlines()

from collections import Counter
counters = [ Counter() for x in range(20) ]

def get_counts():
	for l in lines:
		l = l.strip()
		for i in range(len(l)):
			counters[i].update({l[i]: 1})

	return counters

def get_most_common(counters):
	result = ""
	for c in counters:
		if len(c) > 0:
			result += c.most_common(1)[0][0]

	return result
	
def get_least_common(counters):
	result = ""
	for c in counters:
		if len(c) > 0:
			result += c.most_common(1000)[-1][0]

	return result
	
def day6a():
	return get_most_common(get_counts())

def day6b():
	return get_least_common(get_counts())

def main():
	print day6a()
	print day6b()


if __name__=="__main__":
	main()
