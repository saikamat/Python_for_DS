"""
Created on Fri Dec 28 23:11:21 2018
Implmentation of a dynamic linked list.
@author: Sai Kamat
"""
# creating linked list


class Node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next = None    # initially ptr. pts. to nothing.


class SingleLinkedList:
    def __init__(self):
        self.head_val = None

# traverse the list.
    def printList(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next


list1 = SingleLinkedList()
list1.head_val = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


# link 2nd node to the 1st node.
list1.head_val.next = e2

# connect 3rd to second node.
e2.next = e3

# print the list.
list1.printList()
#SingleLinkedList.printList()   # incorrect way of invoking method.
