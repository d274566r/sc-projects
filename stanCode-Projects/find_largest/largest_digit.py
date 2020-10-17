"""
File: largest_digit.py
Name:謝濡駿
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
largest = 0


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: The number that user entered.
	:return: The largest digit in the number.
	"""
	global largest
	n = int((n**2)**0.5)  # making all integers > 0
	if n % 10 == (n//10) % 10 and n < largest:
		print(largest)
		largest = 0  # Reset the param 'largest'
	else:
		if n % 10 > largest:
			largest = n % 10
		find_largest_digit(n//10)


if __name__ == '__main__':
	main()
