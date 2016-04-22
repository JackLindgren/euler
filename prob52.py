def isPermMult(x):
	a = sorted(list(str(x)))
	b = sorted(list(str(x * 2)))
	c = sorted(list(str(x * 3)))
	d = sorted(list(str(x * 4)))
	e = sorted(list(str(x * 5)))
	f = sorted(list(str(x * 6)))
	return a == b == c == d == e == f

def main():
	for a in range(100,167):
		if isPermMult(a):
			return a
	for b in range(1000,1667):
		if isPermMult(b):
			return b
	for c in range(10000,16667):
		if isPermMult(c):
			return c
	for d in range(100000,166667):
		if isPermMult(d):
			return d

print main()