'''
Reversing a singly linked list.
'''


'''
For testing purposes.
'''
class LinkedNode(object):
	data = None 
	next = None
	def __init__(self, data):
		self.data = data

class LinkedList(object):
	head = None
	tail = None

	def add(self, node):
		if type(node) is LinkedNode:
			if self.tail == None:
				self.head = node
				self.tail = node
			elif type(self.tail) is LinkedNode:
				self.tail.next = node
				self.tail = node	

	def print_nodes(self):
		curr = self.head
		ans = ''
		while curr != None:
			ans += str(curr.data) + ' -> '
			curr = curr.next
		print(ans + 'None')


''' Reverses linked list in-place in O(n) time. '''
def reverse(ll):
	prev = ll.head
	if prev != None:
		curr = prev.next
		while curr != None:
			ll.head.next = curr.next
			curr.next = prev
			prev = curr
			curr = ll.head.next
	ll.head = prev




''' Test 0 '''
list0 = LinkedList()
list0.print_nodes()
reverse(list0)
list0.print_nodes()
print()

''' Test 1 '''
list1 = LinkedList()
list1.add(LinkedNode(1))
list1.print_nodes()
reverse(list1)
list1.print_nodes()
print()

''' Test 2 '''
list2 = LinkedList()
for i in range(1, 6):
	list2.add(LinkedNode(i))
list2.print_nodes()
reverse(list2)
list2.print_nodes()
print()
