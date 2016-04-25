tries = ["319", "680", "180", "690", "129", "620", "762", "689", "762", "318", "368", "710", "720", "710", "629", "168", "160", "689", "716", "731", "736", "729", "316", "729", "729", "710", "769", "290", "719", "680", "318", "389", "162", "289", "162", "718", "729", "319", "790", "680", "890", "362", "319", "760", "316", "729", "380", "319", "728", "716"]

pairs = []

def dedupe(lol): # list of lists
	result = []
	for l in lol:
		if l not in result:
			result.append(l)
	return result

for o in range(0,10):
	for i in range(0,10):
		for t in tries:
			if str(o) in t and str(i) in t:
				if list(t).index(str(o)) > list(t).index(str(i)):
					pairs.append([i, o])
				elif list(t).index(str(i)) > list(t).index(str(o)):
					pairs.append([o, i])

for i in range(0,10):
	numAfter = []
	for p in dedupe(pairs):
		if p[0] == i:
			numAfter.append(p[1])
	print "Comes after  {0}:".format(i), numAfter

for i in range(0,10):
	numBefore = []
	for p in dedupe(pairs):
		if p[1] == i:
			numBefore.append(p[0])
	print "Comes before {0}:".format(i), numBefore

# put them into lists somehow
# check for numbers that have nothing in the before or after
# find the number with the maximum length of its "after" list - this is the first value
# the next number is number with the shortest non-zero "before" list
# the last number is the number with the longest "before" list
# 