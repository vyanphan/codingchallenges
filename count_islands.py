'''
Given a 2D array of 0s and 1s, count the number
of 1-islands.

0 1 0 0 0	
1 1 1 0 0  
0 0 0 1 1	  	
0 0 0 0 0
1 0 1 1 0

This has 4 islands (diagonals don't count).
'''

def neighbors(arr,r,c):
	ans = []
	if r-1 >= 0 and arr[r-1][c]==1:
		ans += [(r-1,c)]
	if r+1 < len(arr) and arr[r+1][c]==1:
		ans += [(r+1,c)]
	if c-1 >= 0 and arr[r][c-1]==1:
		ans += [(r,c-1)]
	if c+1 < len(arr[r]) and arr[r][c+1]==1:
		ans += [(r,c+1)]
	return ans

def travel_island(arr,r,c):
	nb = neighbors(arr,r,c)
	for n in nb:
		arr[n[0]][n[1]] = 0
		travel_island(arr,n[0],n[1])

def count_islands(arr):
	ans = 0
	for r in range(len(arr)):
		for c in range(len(arr[r])):
			if arr[r][c]==1:
				ans += 1
				travel_island(arr,r,c)
	return ans


arr = [[0,1,0,0,0],
	   [1,1,1,0,0],
	   [0,0,0,1,1],
	   [1,0,1,0,0]]
print(count_islands(arr))