
from collections import *

graph = defaultdict(list)
with open('day12input.txt') as f:
	for line in f:
		words = line.strip().split()
		a = int(words[0])
		bs = map(lambda x: int(x.strip(',')), words[2:])
		for b in bs:
			graph[a].append(b)
			graph[b].append(a)

vis = set()
ans = 0
for i in range(2000):
	if i in vis:
		continue
	ans += 1
	
	q = [i]
	while q:
		a = q.pop()
		for b in graph[a]:
			if b not in vis:
				vis.add(b)
				q.append(b)
print()
print(ans)
