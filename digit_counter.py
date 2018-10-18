import math

'''
NOT DONE

Let s = concat all numbers from 1 to N.
Return k = s.count(digit d)

Now, given (d, k) calculate the range of N that
would work. 
'''

def count(n,d):
	d = str(d)
	ans = 0
	for x in range(1,n+1):
		ans += str(x).count(d)
	return ans


def test(d,k):
	if d==0:
		d = 10
	power = math.floor(math.log(k,10))
	count_factor = power * 10 ** (power-1)
	count = count_factor * d + 1
	print(power, count_factor, count)

k = count(4000,4)
print(k)
test(4,k)
