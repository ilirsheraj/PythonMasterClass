def my_odds():
	start = 1
	while True:
		yield start
		start += 2


# odd_num = my_odds()
# for i in range(100):
# 	print(next(odd_num))


def pi_series():
	odds = my_odds()
	approximation = 0
	while True:
		approximation += (4 / next(odds))
		yield approximation
		approximation -= (4 / next(odds))
		yield approximation


approx_pi = pi_series()

for x in range(10000000):
	print(next(approx_pi))
