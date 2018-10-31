'''
Given a compressed string in which a number
followed by [] indicate how many times those
characters occur, decompress the string

e.g. : a3[b2[c1[d]]]e --> abcdcdbcdcdbcdcde.

Assume the string is well formed and number will
always be followed by a [].
'''

# O(n) solution, parses [] as empty string
def decompress(s):
	global i
	i = 0
	def decompress_helper():
		global i
		ans = ''
		while i < len(s):
			try:
				t = int(s[i])
				i += 1
				if s[i] != ']':
					i += 1 # skip past opening bracket
					ans += t * decompress_helper()
				else:
					return ans 
			except:
				if s[i] == ']':
					return ans
				else:
					ans += s[i]
			i += 1
		return ans
	return decompress_helper()

print(decompress('1[]'))
print(decompress('1[a] b 3[c 4[def] g 2[hi] j] 2[k 3[l]] mn'))
print(decompress('1[a] b 3[c 4[def8[]]9[] g 2[hi] j] 2[k 3[l]] mn'))
print(decompress('a3[b2[c1[d]]]e'))
