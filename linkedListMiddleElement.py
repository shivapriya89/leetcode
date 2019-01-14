class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def middleNode(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        print(slow.data)
        return slow

ll=LinkedList()
ll.push(1)
ll.push(2)
ll.push(9)
ll.push(4)
ll.push(5)
ll.middleNode()