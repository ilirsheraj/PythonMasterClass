import timeit
from statistics import mean, stdev


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
	list1 = timeit.repeat("x = fact(130)", setup="from __main__ import fact", number=10000, repeat=6)
	list2 = timeit.repeat("x = factorial(130)", setup="from __main__ import factorial", number=10000, repeat=6)

	print(sum(list1))
	print(sum(list2))

	print(mean(list1), stdev(list1))
	print(mean(list2), stdev(list2))
