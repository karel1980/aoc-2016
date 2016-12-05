
import re

lines = open('input').readlines()

from collections import Counter

def rot_n(text, n):
	return "".join([ chr(97 + ((ord(c)-97) + n) % 26) for c in text ])

sum = 0

for l in lines:
	match = re.match('(.*)-(.*)\\[([a-z]{5})\]', l)
	code,room,check =  match.groups()
	
	code = code.replace('-','')

	top5 = Counter(list(code)).most_common(999999)

	top5.sort(key=lambda a: (-a[1],a[0]))
	
	mycheck = "".join(map(lambda a: a[0], top5[:5]))
	if check == mycheck:
		sum += int(room)

	room_id = int(room)
	decrypted = rot_n(code, room_id)
	if (decrypted.startswith('northpoleobjects')):
		print room_id

print sum
