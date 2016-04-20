import math

limit = 500000
limroot = int(math.sqrt(limit))
primes = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		primes[x] = False

firstThousand = []
for i in range(2,10000):
	if primes[i] == True:
		firstThousand.append(i)

def primeFactors(num):
	factors = []
	cp = 0 # "current prime" index - counts us through the prime list
	if primes[num] == True:
		return [num]
	while not primes[num]:
		if num % firstThousand[cp] == 0:
			factors.append(firstThousand[cp])
			num = num / firstThousand[cp]
		if num % firstThousand[cp] != 0: 		# if it doesn't work, let's try the next prime
			cp += 1
	factors.append(num)
	return len(list(set(factors)))

done = False
i = 1
while done != True:
	if primeFactors(i) == 4:
		if primeFactors(i + 1) == 4:
			if primeFactors(i + 2) == 4:
				if primeFactors(i + 3) == 4:
					done = True
					print i
	print i
	i += 1

print "answer is:", i - 1