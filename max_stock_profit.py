import numpy as np

'''
This problem was asked by Facebook.

Given a array of numbers representing the stock
prices of a company in chronological order,
write a function that calculates the maximum
profit you could have made from buying and
selling that stock once. You must buy before you
can sell it.

For example, given [9, 11, 8, 5, 7, 10], you
should return 5, since you could buy the stock
at $5 and sell it at $10.
'''


'''
For correctness tests.
'''
def naive_solution(prices):
    best = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best

'''
Let arr[i] be some value and arr[i+k] be a later
value time-wise.

If arr[i] < arr[i+k] you know arr[i+k] CANNOT be
the minimum buy point, because whatever you sell
it for you always could have bought it for less
at arr[i].

Only if arr[i+k] < arr[i] should you consider it
a new potential minimum. If this happens, the new
potential minimum should only be chosen if you
get a better glob_dif at some value after arr[i+k].

You do not have to check any of the sell values
before arr[i+k] because you can't sell before you
buy.

You only need to check if a sale after arr[i+k]
will give you a better profit. If so, you can
discard the previous minimum arr[i] because
whatever you sell it for, you could always have
bought it for cheaper at arr[i+k].

The below solution runs in O(n) time.
'''
def linear_solution(arr):
    curr_min = arr[0]
    glob_min = arr[0]
    glob_dif = 0
    for x in arr[1:]:
        if x < curr_min:
            curr_min = x
        if x - curr_min > glob_dif:
            glob_min = curr_min
            glob_dif = x - curr_min
    return glob_dif

'''
Correctness test
'''
for i in range(1000):
    random_arr = np.random.randint(0, 100, size=100)
    if(naive_solution(random_arr) != linear_solution(random_arr)):
        print('bad')