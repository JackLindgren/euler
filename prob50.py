import math

# get some primes
limit = 1000000	
limroot = int(math.sqrt(limit))
primes = [True] * limit

for i in range(2, limroot + 1):
	for x in range(i + i, limit, i):
		primes[x] = False

# put those primes in a list
actualPrimes = []
for i in range(2,50000):
	if primes[i] == True:
		actualPrimes.append(i)

# store our current record setter
longestPrime = {"prime":0, "length":0}

# check all the combinations, dumbly
for op in actualPrimes:
	sequence_length = 1
	sequence_sum = op
	for ip in actualPrimes[actualPrimes.index(op)+1:]:
		sequence_sum += ip
		sequence_length += 1
		if sequence_sum >= 1000000: # if the sum is >1000000, we've gone to far
			break
		if primes[sequence_sum] and sequence_length > longestPrime["length"] and sequence_length < 1000000:
			# if the sum is under 1000000 
			# and it's number of terms are greater than the current record-setter
			# then it's the new champion
			longestPrime["prime"] = sequence_sum
			longestPrime["length"] = sequence_length

# once we've exhaused our possibilities:
print longestPrime