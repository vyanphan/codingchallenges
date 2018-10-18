def recursive_fib(k):
	if k==0:
		return 0
	elif k==1:
		return 1
	else:
		return recursive_fib(k-1) + recursive_fib(k-2)

def dp_fib(k):
	fibs_so_far = [0,1]
	for i in range(2,k+1):
		fibs_so_far += [fibs_so_far[i-1] + fibs_so_far[i-2]]
	return fibs_so_far[k]

def iter_fib(k):
	a = 0
	b = 1
	for i in range(k):
		a, b = b, a+b
	return a

N = 15
for k in range(N):
	print(recursive_fib(k), dp_fib(k), iter_fib(k))
