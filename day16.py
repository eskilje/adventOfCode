import numpy

def spin(list, n):
	return numpy.roll(list, n)

def exchange(list, x, y):
	list[x], list[y] = list[y], list[x]

def partner(list, x, y):
	indexX = list.index(x) 
	indexY = list.index(y)
	list[indexX], list[indexY] = list[indexY], list[indexX]
letterList = [chr(i) for i in range(ord('a'),ord('p')+1)]
myTest = []
reps = 1000000000
with open('day16input') as f:
	for line in f:
		line = line.split(',')
		for i in range(reps):
			if letterList in myTest:
				print(myTest[reps % i])
				break
			myTest.append(list(letterList))
			for x in line:
				if x[0] == 's':
					letterList = list(spin(letterList, int(x[1:])))
				elif x[0] == 'x':
					x = x[1:]
					x = x.split('/')
					exchange(letterList, int(x[0]), int(x[1]))
				elif x[0] == 'p':
					x = x[1:]
					x = x.split('/')
					partner(letterList, x[0], x[1])