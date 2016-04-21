import math

pentNums = []

for n in range(1,1000000):
	pnum = (n * (3 * n - 1)) / 2
	pentNums.append(pnum)

def isPentNum(num):
  pentest = (math.sqrt(1 + 24 * num) + 1 ) / 6
  return pentest == int(pentest)

for o in pentNums:
  for i in pentNums:
    if isPentNum(o + i):
      if isPentNum(abs(o - i)):
        print o, i


#i = 0
#while (pentNums[i] + pentNums[i + 1] not in pentNums) and (pentNums[i+1] - pentNums[i] not in pentNums):
#	i += 1

#print pentNums[i], pentNums[i + 1]
#print pentNums[i + 1] - pentNums[i]
