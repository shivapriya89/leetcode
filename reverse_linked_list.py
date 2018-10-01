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
        while current.next:
            if current.next.data==data:
                current.next = current.next.next
            else:
                current=current.next

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.pop(4)
llist.push(60)
llist.pop(20)

#print ("Given Linked List")
llist.printList()
#llist.reverse()
#print ("\nReversed Linked List")
#llist.printList()