# -*- coding: utf-8 -*-
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
        print_val = self.head_val   # print_val is value of head node.
        while print_val is not None:
            print(print_val.data_val)
            print_val = print_val.next

# inserting elements into the list
# at the beginning
    def AtBegining(self, new_data):
        NewNode = Node(new_data)
        NewNode.next = self.head_val
        self.head_val = NewNode

# at the end.
    def AtEnd(self, new_data):
        NewNode = Node(new_data)    # create a node.
        if self.head_val is None:   
            # if the head node's value is None, then let the new node be 
            # the head.
            self.head_val = NewNode
            return
        laste = self.head_val
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
                
list1 = SingleLinkedList()
list1.head_val = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


# link 2nd node to the 1st node.
list1.head_val.next = e2

# connect 3rd to second node.
e2.next = e3

# print the list.
print ("\ninitial list...")
list1.printList()
# SingleLinkedList.printList()   # incorrect way of invoking method.


# insert element at the beginning of the list.
list1.AtBegining("Sun")

print("\nafter inserting at head...")
list1.printList()

# insert element at the end of the list.
list1.AtEnd("Thu")

print("\nafter inserting at tail...")
list1.printList()