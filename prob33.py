
def modified(num, den):
  newNum = num / 10
  newDen = den - (den / 10 * 10)
  return [newNum, newDen]

def nonTrivial(num, den):
  if num % 10 == 0 or den % 10 == 0:
    return False
  elif num / 10 == num - num / 10 * 10:
    return False
  elif den / 10 == den - den / 10 * 10:
    return False
  elif float(num) / den == 1:
    return False
  else:
    return True

answers = []

for denominator in range(10,100):
  for numerator in range(10,denominator):
    if (numerator % 10 == 0) or (denominator % 10 == 0):
      continue
    new = modified(numerator, denominator)
    if (float(new[0]) / new[1] == float(numerator) / denominator) and (numerator - numerator / 10 * 10 == denominator / 10):
      if nonTrivial(numerator, denominator):
        answers.append([new[0], new[1]])

print answers

prodNum = 1
prodDen = 1

for x in answers:
  prodNum = prodNum * x[0]
  prodDen = prodDen * x[1]

print prodDen / prodNum
