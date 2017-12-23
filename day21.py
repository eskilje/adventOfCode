from collections import defaultdict

def printPic(picToPrint):
	splitted = picToPrint.split('/')
	for row in splitted:
		print(row)

def rotate(picToRotate):
	rotated = list(reversed(list(zip(*picToRotate.split('/')))))
	temp = []
	for row in rotated:
		temp.append(''.join(row))
	return '/'.join(temp)

def flip(picToFlip):
	flipped = list(reversed(picToFlip.split('/')))
	temp = []
	for row in flipped:
		temp.append(''.join(row))
	return '/'.join(temp)

rules = defaultdict(str)
with open('day21input') as f:
	for line in f:
		line = line.strip().split(' => ')
		i = 0
		temp = line[0]
		while temp not in rules:
			rules[temp] = line[1]
			if i < 4:
				temp = rotate(temp)
				i += 1
			else:
				temp = flip(temp)
				i = 0
			print(temp)

currentPic = '.#./..#/###'

finalStuff = []
depth = 0

def depthSearch(curDepth, picToStuff):
	print(curDepth)
	print(picToStuff)
	if curDepth == 5:
		finalStuff.append(picToStuff)
	else:		
		picToStuff = rules[picToStuff]
		if len(picToStuff) < 12:
			depthSearch(int(curDepth + 1), picToStuff)
		else:
			depthSearch(int(curDepth + 1), str(picToStuff[0:2] + '/' + picToStuff[5:7]))
			depthSearch(int(curDepth + 1), str(picToStuff[2:4] + '/' + picToStuff[7:9]))
			depthSearch(int(curDepth + 1), str(picToStuff[10:12] + '/' + picToStuff[15:17]))
			depthSearch(int(curDepth + 1), str(picToStuff[12:14] + '/' + picToStuff[17:19]))
depthSearch(0, currentPic)

counter = 0
for line in finalStuff:
	for char in line:
		if char == '#':
			counter += 1
print(counter)
