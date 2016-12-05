import md5

door_id = 'uqwqemis'
#door_id = 'abc'

i = 0
found = 0
digits = ['0','1','2','3','4','5','6','7']
answer = [ '_' for x in range(8) ]
while '_' in answer:
	checksum = md5.new(door_id + str(i)).hexdigest()

	if checksum.startswith('00000'):
		pos = checksum[5:6]
		char = checksum[6:7]

		if pos in digits:
			if answer[int(pos)] == '_':
				answer[int(pos)] = char
				print "".join(answer)

	i+=1

