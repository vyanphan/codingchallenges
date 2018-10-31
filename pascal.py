# Print n rows of Pascal's Triangle.

def pascal(n):
	for line in range(1, n+1):
		c = 1
		s = ""
		for i in range(1, line+1):
			space = (n - line) * "\t"
			s += str(c) + "\t\t"
			c = int(c*(line-i) / i)
		print(space + s + space)

pascal(0)
print()
pascal(1)
print()
pascal(2)
print()
pascal(7)
