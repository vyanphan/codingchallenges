'''
NOT DONE

Given a lower-case only string, delete all but
one of each repeated character such that the
remaining string is smallest lexicographically.

e.g. 'bcabc'
>>> delete 1st b and 1st c to get 'abc'


let n be length of string
let k be number of unique characters (<= 26)
'''

def lexicographic_delete(s):
	best_ans = ""
	curr_ans = ""
	for c in s: # O(26n) = O(n)
		if c not in best_ans: # O(26)
			best_ans += c
		else:
			temp = best_ans.replace(c,'')+c # O(26)
			if temp<best_ans:
				best_ans = temp
		if c not in curr_ans: # O(26)
			curr_ans += c
		else:
			curr_ans = curr_ans.replace(c,'')+c # O(26)
			if curr_ans<best_ans:
				best_ans = curr_ans
	return best_ans

print(lexicographic_delete('bcabc'))
print(lexicographic_delete('cbacdcbc'))
print(lexicographic_delete('cccccc'))
print(lexicographic_delete('badcd'))


'''
def ans2():
	chars = set()
	for c in s:
		chars.add(c)
	chars = list(chars)
	chars.sort()
	
	start = s.index(chars[0])
	ans = [start]
	for c in chars[1:]:
		i = start + 1
		while s[i] != c:
			i = (i+1) % len(s)
		ans += [i]

	ans.sort()
	return ''.join([s[i] for i in ans])
'''
