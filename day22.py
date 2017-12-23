from collections import defaultdict

nodes = defaultdict(lambda: '.')

with open('day22input') as f:
	y = 0
	for line in f:
		line = line.strip()
		x = 0
		for char in line:
			nodes[(y,x)] = char 	
			x += 1
		y += 1

curPos = (12,12)
curDir = (-1, 0)
infectedCounter = 0
for _ in range(10000000):
	if nodes[curPos] == '#': # GO RIGHT
		if curDir == (1, 0): # ner
			curDir = (0, -1)
		elif curDir == (0, -1): # vänster
			curDir = (-1, 0)
		elif curDir == (-1, 0): # up
			curDir = (0, 1)
		elif curDir == (0, 1): # höger
			curDir = (1, 0)		
		nodes[curPos] = 'f'		
	elif nodes[curPos] == '.': # GO LEFT
		if curDir == (1, 0): # ner
			curDir = (0, 1)
		elif curDir == (0, 1): # höger
			curDir = (-1, 0)
		elif curDir == (-1, 0): # up
			curDir = (0, -1)
		elif curDir == (0, -1): # vänster
			curDir = (1, 0)
		nodes[curPos] = 'w'		
	elif nodes[curPos] == 'f':
		curDir = (curDir[0] * -1, curDir[1] * -1)
		nodes[curPos] = '.'
	elif nodes[curPos] == 'w':
		nodes[curPos] = '#'
		infectedCounter += 1
	curPos = (curPos[0] + curDir[0], curPos[1] + curDir[1])
print(infectedCounter)