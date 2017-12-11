#Task 1 & 2
import sys

myInput = sys.stdin.readline()

depth = 0
skip = False
garbage = False
garbageChar = 0
score = 0
leftBracketList = []
for char in myInput:
  if skip == False:
	if char == '{' and garbage != True:
  	depth += 1
  	leftBracketList.append('{')
	elif char == '<' and garbage != True:
  	garbage = True
	elif char == '!':
  	skip = True
	elif char == '}' and garbage != True:
  	leftBracketList.pop()
  	score += depth
  	depth -= 1
	elif char == '>':
  	garbage = False
	elif garbage == True:
  	garbageChar += 1
  else:
	skip = False
    
print(score, garbageChar)
