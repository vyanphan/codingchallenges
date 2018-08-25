import numpy as np

def best_sell_naive(prices):
    best = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best

def best_sell(prices):
    global_min = global_max = prices[0]
    best_profit = 0
    for ele in prices:
        if ele > global_max:
            global_max = ele
            best_profit = max(best_profit, global_max - global_min)
        elif ele < global_min:
            global_min = global_max = ele
    return best_profit

def max_profit(arr):
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


for i in range(1000):
    random_arr = np.random.randint(0, 100, size=100)
    if(best_sell(random_arr) != max_profit(random_arr)):
        print('bad')