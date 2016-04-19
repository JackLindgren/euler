answers = []
for x in range(10, 355001):
  sum = 0
  for y in list(str(x)):
    sum += int(y) ** 5
  if sum == x:
    answers.append(x)

print answers

answer = 0
for a in answers:
  answer += a

print answer
