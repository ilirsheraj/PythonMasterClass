def bubble_sort(data: list) -> None:
	""" Sorts a list in place"""
	n = len(data)
	comparison_count = 0
	for i in range(n-1):
		for j in range(n - 1):
			comparison_count += 1
			if data[j] > data[j + 1]:
				data[j], data[j + 1] = data[j + 1], data[j]
		print(f"End of pass {i}. 'data' is now {data}")
	print(f"comparison_count is {comparison_count}")


numbers = [3, 2, 4, 1, 5, 7, 6]
print(f"Sorting{numbers}")
bubble_sort(numbers)
print(f"The sorted data is {numbers}")
