class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self):
        fast=slow=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
        return slow

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,)
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
llist.push(37)
llist.push(99)
llist.push(7)
llist.push(62)
#llist.push(41)
llist.printList()
print('Middle node')
llist.middleNode()
