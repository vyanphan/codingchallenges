'''
This problem was asked by Two Sigma.

Using a function rand5() that returns an integer
from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an
integer from 1 to 7 (inclusive).
'''

'''
Works, but nondeterministic time.

Use rand5() to build a rand2() function, then use
the rand2() function as a random bit generator.

A three-bit number can represent anything from 0
to 7. If 0, regenerate, otherwise return.
'''
def nondeterministic_time_solution():
	def rand2():
	    x = 5
	    while x == 5:
	        x = rand5()
	    return x // 2
    x = 0
    while x == 0:
         x = 4 * rand2() + 2 * rand2() + rand2()
    return x

def markov_chain_solution():
	# probably exists but i'm lazy