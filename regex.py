'''
Make a simple regex function that matches * and +

+ matches any single or empty character
* matches any sequence (including empty)

text: 'baaabab'

regex: 'baa*a++'	True
regex: 'ba*a+'		True
regex: 'a*ab'		False
'''
def regex_match_recursive(string, regex):
	if string == ''  and regex == '':
		return True
	elif len(string)<1:
		for c in regex:
			if c != '*' and c != '+':
				return False
		return True
	elif len(regex)<1:
		return False
	else:
		if string[0]==regex[0]:
			return regex_match_recursive(string[1:],regex[1:])
		elif regex[0]=='+':
			return regex_match_recursive(string[0:], regex[1:]) \
				or regex_match_recursive(string[1:], regex[1:])
		elif regex[0]=='*':
			for i in range(len(string)):
				if regex_match_recursive(string[i:], regex[1:]):
					return True
		else:
			return False


def regex_match_dp(string, regex):
	matches = [None] * len(string)
	

print(regex_match_recursive('baaabab', 'baa*a++'))
print(regex_match_recursive('baaabab', 'baa*b++'))
print(regex_match_recursive('baaabab', 'baa*b+'))
print(regex_match_recursive('baaabab', 'ba*a+'))
print(regex_match_recursive('baaabab', 'ba*a++'))
print(regex_match_recursive('', '*'))
print(regex_match_recursive('', '***'))
print(regex_match_recursive('', '+'))
print(regex_match_recursive('', '+++'))
print(regex_match_recursive('a', ''))
print(regex_match_recursive('', '+++a'))
print(regex_match_recursive('', '*ab'))
print(regex_match_recursive('baaabab', 'a*ab'))


# def regex_match_dp(string, regex):
# 	matches = [None] * len(string)
# 	if string==regex:
# 		return True
# 	i = 0 # string index
# 	j = 0 # regex index
# 	while i < len(string):
# 		if string[i] == regex[j]:
# 			i += 1
# 			j += 1
# 			matches[i] = True
# 		elif regex[j] == '+':
# 			return regex_match(string[i:], regex[j+1:]) \
# 				or regex_match(string[i+1:], regex[j+1:])
# 		elif regex[j] == '*':
