#Task 1 & 2
import sys

operations = {
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    '<': lambda x, y: x < y,
    '<=': lambda x, y: x <= y,
    '>': lambda x, y: x > y,
    '>=': lambda x, y: x >= y
}
max1 = 0
registers = dict()
while True:
  myInput = sys.stdin.readline()
  if myInput == "EOF\n":
    break
  myInput = myInput.split()
  if myInput[4] not in registers:
    registers[myInput[4]] = 0
  print(myInput[4], " ", myInput[5], " ", myInput[6])
  if operations[myInput[5]](registers.get(myInput[4]), int(myInput[6])):
    if myInput[0] not in registers:
      registers[myInput[0]] = 0
    if myInput[1] == 'inc':
      registers[myInput[0]] += int(myInput[2])
    else:
      registers[myInput[0]] -= int(myInput[2])
    if registers[myInput[0]] > max1:
      max1 = registers[myInput[0]]

print(max(registers.values()))
print(max1)
