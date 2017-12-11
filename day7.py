#Task 1
import sys

listOfNumbers = []
supporter = []
supportee = []
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":	
  	break
	myInput = myInput.rstrip().split()
	supporter.append(myInput[0])
	if len(myInput) > 2:
  	for x in range(3, len(myInput)):
    	supportee.append(myInput[x].replace(",",""))
	listOfNumbers.append(myInput)

print(set(supporter) - set(supportee))

#Task 2
import sys

def totalWeight(label):
    totW = 0

    subs = {}
    for sub in holding[label]:
        if(sub in holding):
            subs[sub] = totalWeight(sub)
        else:
            subs[sub] = weights[sub]

    x = 0
    s = next(iter(subs))
    w = subs[s]
    for s_ in subs:
        if(subs[s_] is not w):
            x += subs[s_] - w
            if (x is not 0):
                subs[s_] -= x
                weights[s_] -= x
                print("Part two:", weights[s_])

    for s in subs:
        totW += subs[s]
    totW += weights[label]

    return totW

holding = {}
weights = {}
while True:
	myInput = sys.stdin.readline()
	if myInput == "EOF\n":
	  break
	count = 0
	hold = set()
	for word in myInput.split():
	  if(count == 0):
	    name = str(word)
	  elif(count == 1):
	    weights[name] = int(word.strip('()'))
	  else:
	    if(len(word) is not 2):
	      hold.add(word.strip(','))
	  count += 1
	if(len(hold) > 0):
	  holding[name] = hold

print(totalWeight('bpvhwhh'))

