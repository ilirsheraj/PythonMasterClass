import timeit


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
	print(timeit.timeit("x = fact(130)", setup="from __main__ import fact", number=10000))
	print(timeit.timeit("x = factorial(130)", setup="from __main__ import factorial", number=10000))
