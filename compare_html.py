'''
Given a tree representation of a html parsed
output, wherein every block is a node in the
tree, find if two html docs contain the same
text.

struct Node {
       string value;
       bool isMetadata;
       vector<Node*> children;
};

ex) Consider the two documents:

			value: sample
			metadata: true
	 		/			\
	value: children		value: Hello World
	metadata: true		metadata: true
							\
						value: Hello World
						metadata: false

	This is equivalent to:
		value: Hello World
		metadata: false
'''

'''
Solution: 

Traverse tree 1 and tree 2 simultaneously.
If metadata = true, skip that node and iterate further.
Else, compare current node values.

If current node values are same, continue.
Else, return false.

We assume order of text matters.
'''

'''
e.g.
		F
	/	|	\
	F  [T]	 F
/	|	|	  \
F  [T]	F	   F
	/\			\
   T  T			[T]
'''
def find_nonmetadata_children(node):
	ans = []
	for c in node.children:
		if c.metadata:
			ans += find_children(c)
		else:
			ans += [c]
	return ans


# all inputs to this should be metadata == FALSE
def traverse_html_tree_helper(node1, node2):
	if node1.value != node2.value:
		return False 
	else:
		c1 = find_nonmetadata_children(node1)
		c2 = find_nonmetadata_children(node2)
		if len(c1) != len(c2):
			return False
		for i in range(len(c1)):
			if not traverse_html_tree_helper(c1[i], c2[i]):
				return False
		return True


def traverse_html_tree(root1, root2):
	r1, r2 = [root1], [root2]
	if root1.metadata:
		r1 = find_nonmetadata_children(root1)
	if root2.metadata:
		r2 = find_nonmetadata_children(root2)

	if len(r1) != len(r2):
		return False
	for i in range(len(r1)):
		if not traverse_html_tree_helper(r1[i], r2[i]):
			return False
	return True
