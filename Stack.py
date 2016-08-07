## An implementation of a stack as a linked list

class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insertAtHead(self, data):
		copyHead = self.head
		self.head = Node(data)
		self.head.next = copyHead

	def deleteAtHead(self):
		if self.head == None:
			return None

		node = self.head
		self.head = node.next
		return node

	def __call__(self):
		pass

class Stack:
	def __init__(self):
		self.LinkedList = LinkedList()

	def push(self, data):
		self.LinkedList.insertAtHead(data)

	def pop(self):
		deleted = self.LinkedList.deleteAtHead()
		if deleted is None:
			raise Exception("Stack is empty!!")
		else:
			return deleted.data

	def top(self):
		if self.LinkedList.head == None:
			return None
		else:
			return self.LinkedList.head.data

	def __iter__(self):
		return self

	def next(self):
		if self.top() != None:
			return self.pop()
		else:
			raise StopIteration

if __name__ == '__main__':
	stack = Stack()
	arr = map(lambda x: int(x), raw_input().split(" "))

	for a in arr:
		stack.push(a)

	print "Top of stack is: ", stack.top()

	print "Iterate over the stack ?"
	if (raw_input() == "Y"):
		for i in stack:
			print i

	print "Stack top is: ", stack.top()






