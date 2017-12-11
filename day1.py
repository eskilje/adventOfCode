#Task 1
sumTotal = 0
myString = input
index = 0
for c in myString:
  if c == myString[(index + 1) % len(myString)]:
    sumTotal += int(c)
  index += 1
print(sumTotal)

sumTotal = 0

#Task 2
myString = input
index = 0
for c in myString:
  if c == myString[(index + len(myString) / 2) % len(myString)]:
    sumTotal += int(c)
  index += 1
print(sumTotal)
