

input = 'jzgqcdpd'


def hash2(inp):
	text2 = []
	numberList = list(range(256))
	pos = 0
	skip = 0
	for i in range(len(inp)):
		text2.append(ord(inp[i]))
	text2 += [17, 31, 73, 47, 23]
	for _ in range(64):
		for i in text2:
			temp = []
			for j in range(i):
				temp.append(numberList[(pos+j) % 256])
			for j in range(i):
				numberList[(pos+i-1-j) % 256] = temp[j]
			pos += i + skip
			skip += 1
	
	hashList = [0]*16
	for i in range(16):
		hashList[i] = numberList[16 * i]
		for m in range(1, 16):
			hashList[i] ^= numberList[16 * i + m]
	knothash = ''
	for i in hashList:
		if len(hex(i)[2:]) == 2:
			knothash += hex(i)[2:]
		else:
			knothash += '0' + hex(i)[2:]
	return knothash




taken = []
rows = []
for i in range(128):
	hashedRow = hash2(input + '-' + str(i))
	hashedRow = bin(int(hashedRow, 16))[2:].zfill(128)
	rows.append(hashedRow)
	taken += [(i, j) for j, d in enumerate(hashedRow) if d == '1']
print(len(taken))


count = 0
while taken:
	toBeChecked = [taken[0]]
	while toBeChecked:
		(x, y) = toBeChecked.pop()
		if (x, y) in taken:
			taken.remove((x, y))
			toBeChecked += [(x - 1, y), (x+ 1, y), (x, y+1), (x, y-1)]
	count += 1
print(count)



