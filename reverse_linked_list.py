'''
Reversing a singly linked list in-place.
You should be able to do this in O(n) time.

Do not put the items into an array, reverse the
array, and put them back into the linked list.
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


def reverse_tester(n):
	ll = LinkedList()
	for i in range(1, n+1):
		ll.add(LinkedNode(i))
	ll.print_nodes()
	reverse(ll)
	ll.print_nodes()
	print()

reverse_tester(0)
reverse_tester(1)
reverse_tester(2)
reverse_tester(7)
