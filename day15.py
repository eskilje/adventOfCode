a = 634
aFactor = 16807
b = 301
bFactor = 48271
divider = 2147483647
checkerDivider = 65536

aNumbers = []
bNumbers = []

while len(aNumbers) < 5000000:
	a = (a * aFactor) % divider
	if a % 4 == 0:
		aNumbers.append(a)
while len(bNumbers) < 5000000:
	b = (b * bFactor) % divider
	if b % 8 == 0:
		bNumbers.append(b)
print(len(aNumbers), len(bNumbers))
counter = 0
for index in range(len(aNumbers)):
	if aNumbers[index] % checkerDivider == bNumbers[index] % checkerDivider:
		counter += 1
print(counter)