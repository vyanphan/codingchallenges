'''
4. Given a 2D matrix M X N, support two ops:

Query(r1, c1, r2, c2) 
returns the sum of all numbers in rectangle 
	r1,c1	r1,c2
	r2,c1	r2,c2	

Update(r, c) to a new number

Query is frequent op (must be fast)
update is slow op (can be slower)
'''

'''
Idea: store precomputed dictionary of cumulative
sums, with top left corner at (0,0). 

Query will take O(1), at most constant.
Update will take O(n + m), at most linear.
Storage is O(n m)
'''

global arr, R, C, sum_arr
arr = [[1,2,3],[4,5,6],[7,8,9]]
R = len(arr) # for ease of computation
C = len(arr[0])
sum_arr = []

# Note: for extra speed we can make vertical as
# 		well as horizontal unit rectangles
# Extra 0-padded row-0 and col-0
def setup():
	global arr, R, C, sum_arr
	sum_arr = [[0] for r in range(R+1)]
	sum_arr[0] = [0 for c in range(C+1)]
	for r in range(1, R+1):
		for c in range(1, C+1):
			sum_arr[r] += [sum_arr[r-1][c] \
						 + sum_arr[r][c-1] \
						 - sum_arr[r-1][c-1] \
						 + arr[r-1][c-1]]

setup()

# Assume c2 > c1, r2 > r1
# Assume inclusive/inclusive
def query(r1, c1, r2, c2): # O(r2 - r1)
	r2, c2 = r2+1, c2+1
	global sum_arr
	return sum_arr[r2][c2] - sum_arr[r1][c2] - sum_arr[r2][c1] + sum_arr[r1][c1]
print(query(0,1,1,1))


def update(r, c, n): # O(C^2)
	global arr, sum_arr, R, C
	if arr[r][c] == n:
		return # don't waste time!
	for row in range(r+1, C+1):
		for col in range(c+1, C+1):
			sum_arr[row][col] += n - arr[r][c]
	arr[r][c] = n

update(1, 1, 13)
print(sum_arr)
