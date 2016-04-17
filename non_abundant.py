import math

def getDivisors(num):
	# returns a list of unique divisors of "num"
	root = int(math.sqrt(num))
	divisors = [1]
	for test in range(2, root + 1):
		if num % test == 0:
			divisors.append(test)
			divisors.append(num / test)
	if num / root == root and num % root == 0:
		divisors.append(root)
	return list(set(divisors))

def sumDivisors(num):
	# returns the sum of all divisors of "num"
	divs = getDivisors(num)
	total = 0
	for div in divs:
		total += div
	return total

def isAbundant(num):
	# tells us whether "num" is abundant
	if sumDivisors(num) > num:
		return True
	else:
		return False

def getAbundantNumbers():
	# returns a list of abundant numbers below a given limit
	limit = 28123
	abundantNumbers = []
	for x in range(1,limit + 1):
		if isAbundant(x):
			abundantNumbers.append(x)
	return abundantNumbers

def getAbundantSums():
	# returns a list of True/False values
	# where True if the index value can be written as the sum of abundant numbers
	# and False if the index cannot be written as the sum of abundant numbers
	abundants = getAbundantNumbers()
	sums = []
	# set everything to false:
	for i in range(1, 28125):
		sums.append(False)
	# for every sum of two abundant numbers, mark that index True:
	for outer in abundants:
		for inner in abundants:
			if outer + inner <= 28123:
				sums[outer + inner] = True
	return sums

absums = getAbundantSums()
answer = 0
i = 0
while i < len(absums):
	if absums[i] == False:
		answer += i
	i += 1

print answer