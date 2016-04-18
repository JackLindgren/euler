# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p <= 1000, is the number of solutions maximised?

import math

def allSolutions(p):
	solutions = []
	for a in range(1,(p/3 + 1)):
		for b in range(a,p):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == p:
				solutions.append([a, b, c])
	return {len(solutions): p}

solutions = []

for i in range(1,1001):
	solutions.append(allSolutions(i))

print sorted(solutions)[-1]