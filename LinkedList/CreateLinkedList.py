
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None # Initialize next as null



class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            print("Next",temp.next)
            temp = temp.next


if __name__=='__main__':

    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()



'''
    Now next of first Node refers to second.  So they
    both are linked.

    llist.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
'''



