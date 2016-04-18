
def modified(num, den):
  newNum = num / 10
  newDen = den - (den / 10 * 10)
  return [newNum, newDen]

answers = []

for numerator in range(10,100):
  for denominator in range(10,100):
    if (numerator % 10 == 0) or (denominator % 10 == 0):
      continue
    else:
      new = modified(numerator, denominator)
      if new[0] / new[1] == numerator / denominator:
        answers.append([numerator, denominator])
#        answers.append([new[0],new[1]])
	
print answers
