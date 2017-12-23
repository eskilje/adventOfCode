stepsForward = 394

myList = [0]
startPos = 0
lengthOfArray = 1
valueAfterZero = 0
for x in range(1, 50000001):
	startPos = ((startPos + stepsForward) % lengthOfArray) + 1
	lengthOfArray += 1
	if startPos == 1:
		valueAfterZero = x
print(valueAfterZero)