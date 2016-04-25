def factorial(x):
	answer = 1
	for i in range(1,x+1):
		answer = answer * i
	return answer

def nCr(n, r):
	return factorial(n) / (factorial(r) * factorial(n-r) )

results = 0

for n in range(1,101):
	for r in range(1,101):
		if nCr(n, r) > 1000000:
			results += 1

print results 