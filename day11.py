#Task 1 & 2
import sys

myInput = sys.stdin.readline().strip().split(',')

operations = {
	'n': lambda x, y, z : (x, y + 1, z - 1),
	'ne': lambda x, y, z: (x + 1, y, z - 1),
	'se': lambda x, y, z: (x + 1, y - 1, z),
	's': lambda x, y, z: (x, y - 1, z + 1),
	'sw': lambda x, y, z: (x - 1, y, z + 1),
	'nw': lambda x, y, z: (x - 1, y + 1, z)
}

pos = (0, 0, 0)

dists = []

print(pos)
for direc in myInput:
  pos = operations[direc](pos[0], pos[1], pos[2])
  dists.append((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)
  print(direc, pos)
 
print((abs(pos[0]) + abs(pos[1]) + abs(pos[2])) / 2)
print(max(dists))
