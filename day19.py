from collections import defaultdict
myMap = []
directions = defaultdict(tuple)
directions['east'] = (0,1)
directions['west'] = (0, -1)
directions['north'] = (-1, 0)
directions['south'] = (1, 0)
with open('day19input') as f:
	for line in f:
		myMap.append(line.replace('\n', ''))

def getNextPos(pos, direction):
	x = pos[0] + direction[0]
	y = pos[1] + direction[1]
	try:
		test = myMap[x][y]
		if test == ' ':
			return (-1, -1)
		return (x, y)
	except ValueError:
		return (-1, -1)

def changeDir(pos, direction):
	if direction == directions['south'] or direction == directions['north']:
		if getNextPos(pos, directions['west']) != (-1, -1):
			return directions['west']
		else:
			return directions['east']
	else:
		if getNextPos(pos, directions['north']) != (-1, -1):
			return directions['north']
		else:
			return directions['south']

for y in range(len(myMap[0])):
	if myMap[0][y] == '|':
		startPos = (0, y)
currentPos = startPos
currentDirection = directions['south']
mapValues = []
counter = 0
while currentPos != (-1, -1):
	counter += 1
	x, y = currentPos[0], currentPos[1]
	if myMap[x][y] == '+':
		currentDirection = changeDir(currentPos, currentDirection)
	elif myMap[x][y] == '|' or myMap[x][y] == '-':
		pass
	else:
		mapValues.append(myMap[x][y])
	currentPos = getNextPos(currentPos, currentDirection)
print(mapValues, counter)