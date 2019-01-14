class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self, data):
        current=self.head
        prev=None
        while current.next:
            if current.next.data==data:
                current.next = current.next.next
                current.prev=prev
            else:
                current=current.next
                current.prev=current

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(7)
#llist.pop(1)
llist.push(4)
llist.push(5)
#llist.pop(4)

print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nReversed Linked List")
llist.printList()