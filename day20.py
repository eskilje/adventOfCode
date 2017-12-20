from collections import defaultdict

class Particle(object):
	def __init__(self, p, v, a, ind):
		self.p = p
		self.v = v
		self.a = a
		self.index = ind

	def step(self):
		for i in range(3):
			self.v[i] += self.a[i]
			self.p[i] += self.v[i]

	def dist(self):
		return sum([abs(x) for x in self.p])

	def acc(self):
		return sum([abs(x) for x in self.a])

particles = []
i = 0
with open('day20input') as f:
	for line in f:
		line = line.split('=')
		tempPos = line[1][1:-4].split(',')
		tempVol = line[2][1:-4].split(',')
		tempAcc = line[3][1:-2].split(',')
		particles.append(Particle(list(map(int,tempPos)), list(map(int,tempVol)), list(map(int,tempAcc)), i))
		i += 1
		
for _ in range(10000):
	partPos = defaultdict(list)
	for particle in particles:
		partPos[tuple(particle.p)].append(particle)
		particle.step()
	particles = []
	for k, v in partPos.items():
		if len(v) == 1:
			particles.append(v[0])
	print(len(particles))

