import math

limit = 10000000
limroot = int(math.sqrt(limit))
primes = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		primes[x] = False

incrementer = 2
corners = [3]

def primeratio(nums):
	primeCount = 0
	compsCount  = 0
	for num in nums:
		if primes[num]:
			primeCount += 1
		elif primes[num] == False:
			compsCount += 1
	return float(primeCount) / compsCount

def primeCount(nums):
	count = 0
	for num in nums:
		if primes[num]:
			count += 1
	return count

def compsCount(nums):
	count = 0
	for num in nums:
		if primes[num] == False:
			count += 1
	return count


x = 3
while x < 1000000:
	x += incrementer
	corners.append(x)
	if len(corners) % 4 == 0:
		incrementer += 2
		if primeratio(corners) < 0.1:
			# print primeCount(corners)
			# print compsCount(corners)
			# print primeratio(corners)
			break

layer = len(corners) / 4
sidelength = layer * 2 + 1

# print "corners:", corners
print "layer:", layer
print "side length:", sidelength
print "prime ratio:", primeratio(corners)
print "primes:", primeCount(corners)
print "non-primes:", compsCount(corners)