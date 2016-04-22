def digSum(x):
	strfm = list(str(x))
	ans = 0
	for d in strfm:
		ans += int(d)
	return ans

largest = 0

for a in range(1,100):
	for b in range(1,100):
		c = digSum(a ** b)
		if c > largest:
			largest = c

print largest

