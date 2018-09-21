'''
Given a binary matrix, find there exists any
rectangle or square in the given matrix whose all
four corners are equal to 1.
'''

def find_rect(m):
	x_edges = []
	for i in range(len(m)):
		y_corners = set()
		for j in range(len(m[i])):
			if m[i][j] == 1:
				y_corners.add(j)
		if len(y_corners)>1:
			x_edges += [y_corners]
		else:
			x_edges += [set()]
	for i in range(len(x_edges)):
		for j in range(i+1, len(x_edges)):
			y_edges = x_edges[i].intersection(x_edges[j])
			if len(y_edges) > 1:
				print('\nYes')
				return [x[min(y_edges):max(y_edges)+1] for x in m[i:j+1]]
	print('\nNo')
	return [[]]


		
	# for i in range(x_edges):
	# 	for j in range(i+1, x_edges):



def print_rect(r):
	print('[' + str(r[0]) + ',')
	for i in range(1, len(r)-1):
		print(' ' + str(r[i]) + ',')
	print(' ' + str(r[len(r)-1]) + ']')



mat1 = [[1, 0, 0, 1, 0],
		[0, 0, 1, 0, 1],
		[0, 0, 0, 1, 0],
		[1, 0, 1, 0, 1]]

print_rect(find_rect(mat1))

mat2 = [[]]
print_rect(find_rect(mat2))

mat3 = [[1]]
print_rect(find_rect(mat3))

mat4 = [[1, 0, 0, 1, 0],
		[0, 0, 1, 0, 1],
		[0, 0, 0, 1, 0],
		[1, 0, 1, 1, 0]]
print_rect(find_rect(mat4))

mat5 = [[1, 0, 0, 1, 0],
		[0, 0, 1, 0, 1],
		[0, 0, 0, 1, 0],
		[1, 0, 1, 0, 0]]
print_rect(find_rect(mat5))