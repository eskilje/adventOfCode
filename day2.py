#Task 1
c = input
sumTotal = 0
for b in c:
  min = 999999
  max = 0
  for a in b:
	if a > max:
  	max = a
	if a < min:
  	min = a
  sumTotal += max - min
print sumTotal

#Task 2
import itertools

rows = input

print(sum(b//a for row in rows for a, b in itertools.combinations(sorted(row), 2) if b%a==0))
