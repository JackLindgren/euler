def factorial(n):
	ans = 1.0
	for i in range(1, n+1):
		ans = ans * i
	return ans

def choose(n, k):
	return factorial(n) / ( factorial(k) * factorial(n-k) )

print 7.0 * (1 - (choose(60,20) / choose(70, 20) ) )