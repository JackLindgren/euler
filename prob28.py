limit = 1001 * 1001

diagVals = [1]

numCounted = 0

countby = 2

i = 1

while i < limit:
	i += countby
	numCounted += 1
	diagVals.append(i)
	if numCounted == 4:
		countby += 2
		numCounted = 0

print diagVals


totalSum = 0

for v in diagVals:
	totalSum += v

print totalSum