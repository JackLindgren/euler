answers = []

for num in range(1,1000):
  decimals = []
  remainders = []
  numerator = 10

  ok = True
  while ok:
    quotient = numerator / num
    decimals.append(quotient)
    remainder = numerator % num
    if remainder in remainders:
      ok = False
    remainders.append(remainder)
    numerator = remainder * 10
    if numerator == 10:
      ok = False

  answers.append([len(decimals), num])

print sorted(answers)[-1][1]
