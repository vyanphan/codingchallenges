# Mergesort
def merge(arr1, arr2):
	print(arr1, arr2)
	i, j, ans = 0, 0, []
	while i<len(arr1) and j<len(arr2):
		if arr1[i] < arr2[j]:
			ans.append(arr1[i])
			i += 1
		else:
			ans.append(arr2[j])
			j += 1
	if i<len(arr1):
		ans += arr1[i:]
	else:
		ans += arr2[j:]
	return ans

def mergesort(arr):
	if len(arr) < 2:
		return arr
	else:
		return merge(mergesort(arr[:len(arr)//2]), mergesort(arr[len(arr)//2:]))



# quicksort
def partition(arr, lo, hi):
	pivot = arr[lo]
	L = lo+1
	R = hi

	while True:
		while L <= R and arr[L] <= pivot:
			L += 1
		while L <= R and pivot <= arr[R]:
			R -= 1
		if R < L:
			break
		else:
			arr[L], arr[R] = arr[R], arr[L]
	arr[lo], arr[R] = arr[R], arr[lo]
	return R

def quicksort_helper(arr, lo, hi):
	if lo < hi:
		pivot = partition(arr, lo, hi)
		quicksort_helper(arr, lo, pivot-1)
		quicksort_helper(arr, pivot+1, hi)
	return arr
	
def quicksort(arr):
	return quicksort_helper(arr, 0, len(arr)-1)





# test
arr = [9,2,3,8,5,6,7,1,2,3,1,6,3]
print(quicksort(arr))
arr.sort()
print(arr)
