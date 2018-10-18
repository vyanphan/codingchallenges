# Z algorithm
def Z_algorithm(s):
    Z = [0] * len(s)
    Z[0] = len(s)
    R, L = 0,0
    for k in range(1, len(s)):
        if k > R: # k > current Z-box, do naive computation.
            n = 0
            while n+k < len(s) and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                L = k
                R = k+n-1
        else: # k inside current Z box
            p = k - L  # pair index
            right_part_len = R - k + 1
            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = R + 1
                while i < len(s) and s[i] == s[i-k]:
                    i += 1
                Z[k] = i-k
                L, R = k, i-1
    return Z


# build suffix tree
def suffix_tree(s):
    pass

# build suffix array
from itertools import zip_longest, islice
def to_int_keys_best(l):
    seen = set()
    ls = []
    for e in l:
        if not e in seen:
            ls.append(e)
            seen.add(e)
    ls.sort()
    index = {v: i for i, v in enumerate(ls)}
    return [index[v] for v in l]
def suffix_array(s):
    n = len(s)
    k = 1
    line = to_int_keys_best(s)
    while max(line) < n - 1:
        line = to_int_keys_best(
            [a * (n + 1) + b + 1
             for (a, b) in
             zip_longest(line, islice(line, k, None),fillvalue=-1)])
        k <<= 1
    return line


# DP, O(MN)
def longest_common_substring(s,t):
    sub_arr = [[0 for _ in  range(len(t)+1)] for _ in range(len(s)+1)]
    max_len = 0
    max_ind = 0
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1]==t[j-1]:
                sub_arr[i][j] = sub_arr[i-1][j-1]+1
                if sub_arr[i][j] > max_len:
                    max_len = sub_arr[i][j]
                    max_ind = j
    return max_len, t[max_ind-max_len:max_ind]



# DP, O(MN)
def longest_common_subsequence(s,t):
    sub_arr = [[0 for _ in  range(len(t)+1)] for _ in range(len(s)+1)]
    max_len = 0
    ans = ''
    for i in range(1,len(s)+1):
        for j in range(1,len(t)+1):
            if s[i-1]==t[j-1]:
                sub_arr[i][j] = sub_arr[i-1][j-1]+1
            else:
                a = sub_arr[i-1][j]
                b = sub_arr[i][j-1]
                if a > b:
                    sub_arr[i][j] = a
                else:
                    sub_arr[i][j] = b
            if sub_arr[i][j] > max_len:
                max_len = sub_arr[i][j]
                ans += t[j-1]
    return max_len, ans

print(longest_common_substring('mississi','lissilsl'))
print(longest_common_substring('turbans','unbanned'))
print(longest_common_subsequence('mississi','lissilsl'))
print(longest_common_subsequence('turbans','unbanned'))
