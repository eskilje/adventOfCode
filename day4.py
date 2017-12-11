#Task 1
import sys

validPhrases = 0
lines = 0
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":
    	break;
	if len(myInput.split()) == len(set(myInput.split())):
  	validPhrases += 1
  	print(myInput)
	lines += 1
print(validPhrases)
print(lines)

#Task 2
import sys
import itertools

stringList = []
wordList = []
count = 0
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":
    	break;
	if len(myInput.split()) == len(set(myInput.split())):
  	stringList.append(myInput.rstrip())

for wordString in stringList:
  continueOrNot = False
  print(wordString)
  wordList = wordString.split()
  for x,y in itertools.combinations(wordList, 2):
	if len(x) == len(y):
  	if set(x) == set(y):
    	continueOrNot = True
  if continueOrNot:
	continue
  else:
	count += 1
print(count)
