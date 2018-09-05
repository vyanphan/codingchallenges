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
from suffix_trees import STree
def suffix_tree_solution(string):
	st = STree.STree(string + '$' + string[::-1] + '#')
	

