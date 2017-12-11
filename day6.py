import sys

previousTries = []
listOfNumbers = sys.stdin.readline().strip().split("\t")
listOfNumbers = list(map(int, listOfNumbers))
controllerList = list(listOfNumbers)
previousTries.append(controllerList)
counter = 0
controller = True

currentList = list(listOfNumbers)
while controller:
  maxVal = -1
  for i in range(len(currentList)):
    if currentList[i] > maxVal:
        maxVal = currentList[i]
        maxIndex = i
        
  currentList[maxIndex] = 0
  
  while maxVal > 0:
    maxIndex = (maxIndex + 1) % len(currentList)
    currentList[maxIndex] += 1
    maxVal -= 1
  
  counter += 1
  
  for listItem in previousTries:
    if currentList == listItem:
      controller = False
  previousTries.append(list(currentList))
print(counter)

#Task 2
import sys

previousTries = []
listOfNumbers = sys.stdin.readline().strip().split("\t")
listOfNumbers = list(map(int, listOfNumbers))
controllerList = list(listOfNumbers)
previousTries.append(controllerList)
counter = 0
controller = True

currentList = list(listOfNumbers)
while controller:
  maxVal = -1
  for i in range(len(currentList)):
    if currentList[i] > maxVal:
        maxVal = currentList[i]
        maxIndex = i
        
  currentList[maxIndex] = 0
  
  while maxVal > 0:
    maxIndex = (maxIndex + 1) % len(currentList)
    currentList[maxIndex] += 1
    maxVal -= 1
  
  counter += 1
  
  for listItem in previousTries:
    if currentList == listItem:
      controller = False
  previousTries.append(list(currentList))
counter = 0
found = False
for listItem in previousTries:
  if listItem == currentList:
    found = True
  if found:
    counter += 1
print(counter)
