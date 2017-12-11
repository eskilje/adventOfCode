#Task 1
import sys

listOfNumbers = []
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":
	  break
	listOfNumbers.append(myInput.rstrip())

listOfNumbers = list(map(int, listOfNumbers))
countJumpsTaken = 0
index = 0
currentAmountOfJumps = 0
while 0 <= index < len(listOfNumbers):
  currentAmountOfJumps = listOfNumbers[index]
  listOfNumbers[index] += 1
  index += currentAmountOfJumps
  countJumpsTaken += 1
  
print(countJumpsTaken)

#Task 2
import sys

listOfNumbers = []
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":
	  break
	listOfNumbers.append(myInput.rstrip())

listOfNumbers = list(map(int, listOfNumbers))
countJumpsTaken = 0
index = 0
currentAmountOfJumps = 0
while 0 <= index < len(listOfNumbers):
  currentAmountOfJumps = listOfNumbers[index]
  
  if currentAmountOfJumps > 2:
    listOfNumbers[index] -= 1
  else:
    listOfNumbers[index] += 1
  index += currentAmountOfJumps
  countJumpsTaken += 1
  
print(countJumpsTaken)
