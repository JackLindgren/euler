#change problem

denominations = [200, 100, 50, 20, 10, 5, 2, 1]

options = 0

for huns in range(1,3):
	for fifties in range(1,5):
		for twen in range(1,11):
			for tens in range(1,21):
				for fives in range(1,41):
					for twos in range(1,101):
						for ones in range(1,201):
							if (huns * 100) + (fifties * 50) + (twen * 20) + (tens * 10) + (fives * 5) + (twos * 2) + (ones) == 200:
								options += 1

print options