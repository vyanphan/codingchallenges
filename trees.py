'''
Red-Black Tree
    Rules
        1.  Root is black
        2.  All leaves black
        3.  All leaves have same black depth to root
        4.  All children of red nodes are black
    Rotation
    Performance
        Searching   O(log n) -- always!
        Insertion   O(log n)
        Deletion    O(log n)
    https://www.cs.usfca.edu/~galles/visualization/RedBlack.html

AVL Tree
    Rotation
        LL: rotate right
        LR: rotate right, then left
        RR: rotate left
        RL: rotate left, then right
    Performance
        Searching   
        Insertion   
        Deletion    

Comparison
    AVL better balanced: use for many lookups, few inserts
    RB easier to insert/delete: less rotations overall
'''

class Node:
	def __init__(self, v):
		self.val = v
		self.L = None
		self.R = None
		self.height = 1

def in_order(node):
	if node:
		return in_order(node.L) + [node.val] + in_order(node.R)
	return []

def pre_order(node):
	if node:
		return [node.val] + pre_order(node.L) + pre_order(node.R)
	return []

def post_order(node):
	if node:
		return post_order(node.L) + post_order(node.R) + [node.val]
	return []


# quick test
root = Node(1) 
root.L = Node(2) 
root.R = Node(3) 
root.L.L = Node(4) 
root.L.R = Node(5) 
root.R.L = Node(6)
root.R.R = Node(7)
print(in_order(root))
print(pre_order(root))
print(post_order(root))




class AVL_Tree(object):
    def insert(self, root, key):
        if not root: # normal BST insert
            return TreeNode(key) 
        elif key < root.val: 
            root.L = self.insert(root.L, key) 
        else: 
            root.R = self.insert(root.R, key) 
  
        # update height
        root.height = 1 + max(self.getHeight(root.L), self.getHeight(root.R)) 
  
        # if unbalanced, rebalance 
        balance = self.getBalance(root) 
        if balance > 1 and key < root.L.val: # case LL
            return self.RRotate(root)
        if balance < -1 and key > root.R.val: # case RR
            return self.LRotate(root)
        if balance > 1 and key > root.L.val: # case LR
            root.L = self.LRotate(root.L) 
            return self.RRotate(root)
        if balance < -1 and key < root.R.val: # case RL
            root.R = self.RRotate(root.R) 
            return self.LRotate(root) 
        return root 

     def delete(self, root, key): 
        if not root: # normal BST delete
            return root 
        elif key < root.val: 
            root.L = self.delete(root.L, key) 
        elif key > root.val: 
            root.R = self.delete(root.R, key) 
        else: 
            if root.L is None: 
                temp, root = root.R, None
                return temp   
            elif root.R is None: 
                temp, root = root.L, None
                return temp   
            temp = self.getMinValueNode(root.R) 
            root.val = temp.val 
            root.R = self.delete(root.R, temp.val) 
   
        if root is None: # if tree only has one node
            return root 
        
        # update ancestor height
        root.height = 1 + max(self.getHeight(root.L), self.getHeight(root.R)) 
  
        # if unbalanced, rebalance
        balance = self.getBalance(root) 
        if balance > 1 and self.getBalance(root.L) >= 0: # case LL
            return self.RRotate(root)
        if balance < -1 and self.getBalance(root.R) <= 0: # case RR
            return self.LRotate(root)
        if balance > 1 and self.getBalance(root.L) < 0: # case LR
            root.L = self.LRotate(root.L) 
            return self.RRotate(root)
        if balance < -1 and self.getBalance(root.R) > 0: # case RL
            root.R = self.RRotate(root.R) 
            return self.LRotate(root) 
        return root
  
    def LRotate(self, z): 
    	y = z.R 
        y.L, z.R = z, y.L 
        z.height = 1 + max(self.getHeight(z.L), self.getHeight(z.R)) 
        y.height = 1 + max(self.getHeight(y.L), self.getHeight(y.R)) 
        return y 
  
    def RRotate(self, z): 
        y = z.L
        y.R, z.L = z, y.R
        z.height = 1 + max(self.getHeight(z.L), self.getHeight(z.R)) 
        y.height = 1 + max(self.getHeight(y.L), self.getHeight(y.R))
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
        return self.getHeight(root.L) - self.getHeight(root.R) 
