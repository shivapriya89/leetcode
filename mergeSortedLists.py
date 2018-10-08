class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

def mergeList(self,l1,l2):
    temp=None
    if l1 is None:
        return l2

    if l2 is None:
        return l1

    if l1.data > l2.data:
        temp=l1
        temp.next = self.mergeList(l2.next,l1)
    else:
        temp=l2
        temp.next = self.mergeList(l2,l1.next)
    return temp

if __name__=='__main__':
    list1 = LinkedList()
    list1.add_node(40)
    list1.add_node(30)
    list1.add_node(25)
    list1.add_node(15)
    print('1st list')
    list1.printList()

    list2 = LinkedList()
    list2.add_node(45)
    list2.add_node(35)
    list2.add_node(20)
    list2.add_node(10)
    print('2nd list')
    list2.printList()

    list3 = LinkedList()
    list3.mergeList(list1,list2)
    print('merge both list')
    list3.printList()
