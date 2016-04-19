# denominations:
# 1
# 2
# 5
# 10
# 20
# 50
# 100
# 200

# Den x Count
# 200 x 1
# 100 x 2
# 50  x 4
# 20  x 10
# 10  x 20
# 5   x 40
# 2   x 100
# 1   x 200

combinations = 0

for one in range(0,201):
	for two in range(one,101):
		for five in range(two,41):
			for ten in range(five,21):
				for twenty in range(ten,11):
					for fifty in range(twenty,5):
						for hundred in range(fifty,3):
							for twohundred in range(hundred,2):
								combinations += 1


print combinations