pentNums = []

for n in range(1,1000000):
	pnum = (n * (3 * n - 1)) / 2
	pentNums.append(pnum)

i = 0
while (pentNums[i] + pentNums[i + 1] not in pentNums) and (pentNums[i+1] - pentNums[i] not in pentNums):
	i += 1

print pentNums[i], pentNums[i + 1]
print pentNums[i + 1] - pentNums[i]