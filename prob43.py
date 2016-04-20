import itertools

results = []

pandigitals = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

def joinNums(digits):
	temp = ""
	for digit in digits:
		temp = temp + str(digit)
	return int(temp)

def divByPrimes(num):
	a = joinNums(num[1:4])
	b = joinNums(num[2:5])
	c = joinNums(num[3:6])
	d = joinNums(num[4:7])
	e = joinNums(num[5:8])
	f = joinNums(num[6:9])
	g = joinNums(num[7:10])
	if (a % 2 == 0) and (b % 3 == 0) and (c % 5 == 0) and (d % 7 == 0) and (e % 11 == 0) and (f % 13 == 0) and (g % 17 == 0):
		results.append(joinNums(num))

for pd in pandigitals:
	if pd[0] != 0:
		divByPrimes(pd)

print results

answer = 0
for r in results:
	answer += r

print answer

