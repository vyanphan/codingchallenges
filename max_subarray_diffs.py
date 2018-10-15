# Given an array of integers. Find two disjoint
# contiguous sub-arrays such that the absolute
# difference between the sum of two sub-array is
# maximum. The sub-arrays should not overlap. 

# arr = [2 -1 -2 1 -4 2 8] 
# ans = [-1 -2 1 -4] [2 8], diff = 16 

def all_same_sign(arr):
	leftSum = arr[0]
	rightSum = sum(arr[1:])
	totalMax = float('-inf')
	for i in range(1, len(arr)):
		a = abs(leftSum - arr[i])
		b = abs(rightSum - arr[i])
		if a > totalMax and a > b:
			totalMax = a
			bestRange = (arr[:i],arr[i:i+1])
		elif b > totalMax and b > a:
			totalMax = b
			bestRange = (arr[i:i+1],arr[i+1:])
		rightSum -= arr[i]
		leftSum += arr[i]
	return bestRange


def find_min_subarray(arr):
	L = 0
	while arr[L] > 0:
		L += 1
	currMin = arr[L]
	currBounds = [L,L+1]
	totalMin = arr[L]
	totalBounds = []
	for i in range(L+1, len(arr)):
		potentialMin = currMin + arr[i]
		if potentialMin < 0:
			currMin = potentialMin
			currBounds[1] = i+1
			if currMin < totalMin:
				totalMin = currMin
				totalBounds = list(currBounds)
		else:
			currMin = arr[i]
			currBounds = [i,i+1]
	return arr[totalBounds[0]:totalBounds[1]]


def find_max_subarray(arr):
	L = 0
	while arr[L] < 0:
		L += 1
	currMax = arr[L]
	currBounds = [L,L+1]
	totalMax = arr[L]
	totalBounds = []
	for i in range(L+1, len(arr)):
		potentialMax = currMax + arr[i]
		if potentialMax > 0:
			currMax = potentialMax
			currBounds[1] = i+1
			if currMax > totalMax:
				totalMax = currMax
				totalBounds = list(currBounds)
		else:
			currMax = arr[i]
			currBounds = [i,i+1]
	return arr[totalBounds[0]:totalBounds[1]]


def find_max_diff_subarrays(arr):
	pos = arr[0] > 0
	for x in arr:
		if (x > 0) != pos:
			return find_min_subarray(arr), find_max_subarray(arr)
	return all_same_sign(arr)


print(find_max_diff_subarrays([2,-1,-2,1,-4,2,8]))
print(find_max_diff_subarrays([6,1,2,2,6]))



# def find_max_subarrays(arr):

	

