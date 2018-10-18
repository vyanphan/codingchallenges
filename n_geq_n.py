import math
'''
NOT DONE

Given an unsorted array of integers n, return the
maximum possible n such that at least n values in
the array are >= n.

[1,2,3,4]
>>> output 2, as 2,3,4 >= 2 but only 3,4 >= 3

[900,2,901,3,1000]
>>> output 3, as 900,901,1000 >= 3
'''

def stupid_n_geq_n(arr): # nlogn solution
	arr.sort(reverse=True)
	for i in range(len(arr)):
		if arr[i] <= i+1:
			return arr[i]
	return None

def n_geq_n(arr):
	return 0


print(n_geq_n([1,2,3,4]))
print(n_geq_n([900,2,901,3,1000]))
print(n_geq_n([1,3,1,1,1,4,5,1,1,1]))
