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

combinations = 1

for onehun in range(0,3):
	for fifty in range(0,5):
		for twenty in range(0,11):
			for ten in range(0,21):
				for five in range(0,41):
					for two in range(0,101):
						for one in range(0,201):
							if (onehun * 100) + (fifty * 50) + (twenty * 20) + (ten * 10) + (five * 5) + (two * 2) + (one * 1) == 200:
								combinations += 1