import math

limit = 2000000
limroot = int(math.sqrt(limit))
isPrime = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		isPrime[x] = False


# aMax = 0
# bMax = 0
# nMax = 0

answers = []

for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = 0
		while isPrime[abs(n*n + a*n + b)]:
			n += 1
		answers.append([n,a,b])
		# if n > nMax:
		# 	aMax = a
		# 	bMax = b
		# 	nMax = n

# print aMax, bMax, nMax

print sorted(answers)[-1]