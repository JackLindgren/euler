import math

limit = 10000
limroot = int(math.sqrt(limit))
primes = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		primes[x] = False

primeNums = []

for x in range(2,limit):
	if primes[x]:
		primeNums.append(x)

doubleSquares = []
for n in range(1,limit):
	doubleSquares.append(n * n * 2)

possibilities = []
for ds in doubleSquares:
	for p in primeNums:
		possibilities.append(p + ds)

for i in range(1, limit, 2):
	if i not in possibilities and primes[i] == False:
		print i
