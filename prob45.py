import math

def isTriangular(num):
	n = (math.sqrt(8 * num + 1) - 1) / 2
	if n == int(n):
		return True
	else:
		return False

def isPentagonal(num):
	n = (math.sqrt(24 * num + 1) + 1) / 6
	if n == int(n):
		return True
	else:
		return False

def isHexagonal(num):
	n = (math.sqrt(8 * num + 1) + 1) / 4
	if n == int(n):
		return True
	else:
		return False

i = 144
done = False

while done == False:
	thisHexagon = i * (2 * i - 1)
	if isPentagonal(thisHexagon) == True:
		if isTriangular(thisHexagon) == True:
			done = True
	else:
		i += 1

print thisHexagon