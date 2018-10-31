'''
Given a contiguous sequence of numbers in which
each number repeats thrice, there is exactly one
missing number. Find the missing number.

11122333 			Missing number 2
11122233344455666	Missing number 5
'''

# for ease, let the numbers be in an array
# i.e. [1,1,1,2,2,3,3,3]

# binary search, O(log n) time, O(1) space
def find_missing_number(arr):
	L = 0
	R = len(arr)
	while True:
		x = (L + R) // 2
		if x+1 >= len(arr) or arr[x+1] != arr[x]:
			if x-2 < 0 or arr[x-2] != arr[x]:
				return arr[x]
			else:
				L = x+1
		elif x-1 < 0 or arr[x-1] != arr[x]:
			if x+2 >= len(arr) or arr[x+2] != arr[x]:
				return arr[x]
			else:
				R = x-1


print(find_missing_number([1,1]))
print(find_missing_number([1,1,1,2,2]))
print(find_missing_number([1,1,2,2,2]))

test1 = [1,1,1,2,2,3,3,3]
print(find_missing_number(test1))

test2 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,6,6,6]
print(find_missing_number(test2))
