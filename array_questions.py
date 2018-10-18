# Find the most frequent integer in an array.
def most_frequent_int(arr):
	counts = {}
	for x in arr:
		if x in counts:
			counts[x] += 1
		else:
			counts.add(x,1)
	return max(counts, key=lambda x:counts[x])

# Find the pair of integers that sums up to S.
def find_pair_sum(arr, S):
	values = set()
	for x in arr:
		if S-x in values:
			return x, S-x
		else:
			values.add(x)
	return None

# Find the subarray of positive integers that sums up to S.
def find_subarr_sum(arr, S):
	if len(arr) < 1: 
		return []
	sum_so_far = arr[0]
	L, R = 0, 1
	while L < len(arr):
		if sum_so_far == S:
			return arr[L:R]
		elif sum_so_far < S:
			if R < len(arr):
				sum_so_far += arr[R]
				R += 1
			else:
				return []
		else:
			sum_so_far -= arr[L]
			L += 1
			if L==R and R<len(arr):
				sum_so_far += arr[R]
				R += 1
	return []

# Find subarray of integers that sums up to S.
def neg_subarr_sum(arr, S):
	if len(arr) < 1: 
		return []

	sum_list = [arr[0]]
	for i in range(1,len(arr)):
		sum_list += [sum_list[i-1] + arr[i]]

	sum_dict = {}
	for i in range(len(sum_list)):
		if sum_list[i] == S:
			return arr[0:i]
		sum_so_far = sum_list[i] - S;
		if sum_so_far in sum_dict:
			return arr[sum_dict[sum_so_far]+1:i+1]
		sum_dict[sum_list[i]] = i
	return []


def largest_subarray_sum(arr):
	glob_max, gL, gR = 0, 0, 0
	curr_max, cL, cR = 0, 0, 0

	for i in range(len(arr)):
		if curr_max + arr[i] < arr[i]:
			curr_max, cL, cR = arr[i], i, i+1
		else:
			curr_max += arr[i]
			cR += 1
		if curr_max > glob_max:
			glob_max, gL, gR = curr_max, cL, cR
	return glob_max, arr[gL:gR]

# print(largest_subarray_sum([2,-3,-1,4,-1,-2,1,-1,2,2,-3,-1,2,2,1,-3,-4,1]))

# assume money and values of arr >= 0
def largest_subarray_under_cost(arr, money):
	gL, gR = 0, 0
	cL, cR = 0, 0
	curr_cost = 0
	while cR < len(arr):
		curr_cost += arr[cR]
		if curr_cost <= money:
			cR += 1
		else:
			while curr_cost > money:
				curr_cost -= arr[cL]
				cL += 1
			if cL > cR:
				cR = cL
		if cR - cL > gR - gL:
			gL, gR = cL, cR
	return gR-gL, arr[gL:gR]
print(largest_subarray_under_cost([1,2,7,16,1,2,3,4], 10))



# should be like above, but instead of storing L,R we store TL,BR corners
# def largest_2D_subarray_under_cost(arr, money):
	









