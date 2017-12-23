securityLevels = []
with open('day13input') as f:
	for line in f:
		line = line.replace(':','').split()
		securityLevels.append([int(line[0]), int(line[1])])

scannerList = []
for item in securityLevels:		
	scannerList.append((item[0], item[1] * 2 - 2))
print(scannerList)

letshopeLOL = 0
caught = True
while caught:
	caught = False
	for item in scannerList:
		#print('this modulo:', item[0], '+', letshopeLOL, '%', item[1], '=', item[0] + letshopeLOL % item[1])
		if (item[0] + letshopeLOL) % item[1] == 0:
			letshopeLOL += 1
			caught = True
			break
print(letshopeLOL)