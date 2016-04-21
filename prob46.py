import math

limit = 10000 # just guessing
limroot = int(math.sqrt(limit))
primes = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		primes[x] = False

# get some primes
primeNums = []

for x in range(2,limit):
	if primes[x]:
		primeNums.append(x)

# get some double squares
doubleSquares = []
for n in range(1,limit):
	doubleSquares.append(n * n * 2)

# get some numbers that _do_ meet the criteria
possibilities = []
for ds in doubleSquares:
	for p in primeNums:
		possibilities.append(p + ds)

# look for numbers that don't
for i in range(1, limit, 2):
	if i not in possibilities and primes[i] == False:
		print i
