"""
@Question 

Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""
# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
# Linked List 
class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert(self, data):
        if(self.head == None):
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = Node(data)

    def display(self):
        temp = self.head
        while(temp != None):
            print temp.data,
            temp = temp.next
        print ""
## Solution Method
    def swap_two_nodes(self):
        prev = None
        right = self.head
        left = right.next
        while(right != None and left != None):
            #swapping 
            temp = left.next
            left.next = right
            right.next = temp
            #connecting with previous value
            if(prev != None):
                prev.next = left
            else: self.head = left
            #preparing for the next iteration
            prev = right
            right = right.next
            if(right!=None): left = right.next  

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.display()
    linked_list.swap_two_nodes()
    linked_list.display()


