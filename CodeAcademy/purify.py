'''Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
For example, purify([1,2,3]) should return [2].
Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.'''

def purify(numbers):
	copy_n = list(numbers)
	len_n = len(copy_n)
	removed = 0
	for i in numbers:
		if i in copy_n and i % 2 != 0:# and i in copy_n:
			copy_n.remove(i)
	return copy_n

#purify([5])

purify([4, 1, 5, 1341, 34, 6, 8])
