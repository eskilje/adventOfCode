securityLevels = []
with open('day13input') as f:
	for line in f:
		line = line.replace(':','').split()
		securityLevels.append([int(line[0]), int(line[1])])
caught = True
delay = 0
level = 0
while caught:
	tempSecurityLevels = list(securityLevels)
	nextLevel = tempSecurityLevels.pop(0)
	while tempSecurityLevels:		
		if (nextLevel[0] + delay) % (nextLevel[1]*2 - 2) == 0:
			break	
		nextLevel = tempSecurityLevels.pop(0)
	if tempSecurityLevels:
		delay += 1
	else:
		caught = False
print(delay)