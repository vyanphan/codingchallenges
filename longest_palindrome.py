'''
This problem was asked by Amazon.

Given a string, find the longest palindromic
contiguous substring. If there are more than one
with the maximum length, return any one.

For example, the longest palindromic substring of
"aabcdcb" is "bcdcb". The longest palindromic
substring of "bananas" is "anana".
'''

'''
For correctness tests.
'''
def naive_solution(string):
	ans = ''
	for i in range(len(string)):
		for j in range(i+1, len(string)+1):
			s = string[i:j]
			if s == s[::-1] and len(s) > len(ans):
				ans = s
	print(ans)


def helper(string, s, e):
	while s >=0 and e < len(string) and string[s] == string[e]:
		s -= 1
		e += 1
	return string[s+1:e]

def better_solution(string): # O(n^2)
	if len(string)<2:
		return string
	longest = string[0]
	for i in range(len(string)):
		temp = helper(string, i, i) # odd length palindrome
		if len(temp) > len(longest):
			longest = temp
		temp = helper(string, i, i+1) # even length palindrome
		if len(temp) > len(longest):
			longest = temp
	print(longest)



'''
A string can be reversed in O(n) time.
Append a string to its reverse (with separators)
and build a combined suffix tree in O(n+k) time
where k is the size of the alphabet.

Traverse the suffix tree in O(n) time to find the
longest common substring of the combined strings.

Since the two strings are reverses, the longest
common substring will be the longest palindromic
substring of the original non-reversed string. 
'''
# from suffix_trees import STree
# def suffix_tree_solution(string):
	# st = STree.STree(string + '$' + string[::-1] + '#')
	


'''
Subsequence characters don't have to be adjacent.
They only have to appear in the same relative order.
'''
def subsequence_helper(string, s, e):
	strlen = e-s
	if strlen < 0:
		return ''
	elif strlen == 0:
		return string[s]
	elif strlen==1 and string[s]==string[e]:
		return string[s:e+1]
	elif string[s] == string[e]:
		return string[s] + subsequence_helper(string, s+1, e-1) + string[e]
	else:
		a = subsequence_helper(string, s, e-1)
		b = subsequence_helper(string, s+1, e)
		if len(a) > len(b):
			return a
		return b

def longest_palindromic_subsequence(string):
	return subsequence_helper(string, 0, len(string)-1)

# print(longest_palindromic_subsequence('ba n ana'))
print(longest_palindromic_subsequence('a man a plan a canal panama'))




