#Task 1 & 2
import sys

myInput = sys.stdin.readline().strip().split(',')

numberList = list(range(256))
pos = 0
skip = 0
myInput = list(map(int, myInput))

for i in myInput:
	temp = []
	for j in range(i):
  	temp.append(numberList[(pos+j) % 256])
	for j in range(i):
  	numberList[(pos+i-1-j) % 256] = temp[j]
	pos += i + skip
	skip += 1
print('Part 1: ', numberList[0]*numberList[1])
print(numberList)

numberList = list(range(256))
pos = 0
skip = 0
inp = '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
text = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
text2 = []

for i in range(len(inp)):
   text2.append(ord(inp[i]))
text2 += [17, 31, 73, 47, 23]
for _ in range(64):
  for i in text2:
	temp = []
	for j in range(i):
  	temp.append(numberList[(pos+j) % 256])
	for j in range(i):
  	numberList[(pos+i-1-j) % 256] = temp[j]
	pos += i + skip
	skip += 1
print(numberList)
hashList = [0]*16
for i in range(16):
  hashList[i] = numberList[16 * i]
  for m in range(1, 16):
	hashList[i] ^= numberList[16 * i + m]

knothash = ''
for i in hashList:
  if len(hex(i)[2:]) == 2:
	knothash += hex(i)[2:]
  else:
	knothash += '0' + hex(i)[2:]
print(knothash)
