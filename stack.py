# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:46:41 2019
Stack implementation
@author: Sai Kamat
"""


class Stack():
    def __init__(self):
        self.items = []     # create a list.

    def isEmpty(self):
        # compares self.items with []. Returns true if equal
        return self.items == []

    def push(self, this_item):
        self.items.append(this_item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def printStack(self):
        for items in reversed(self.items):  # because LIFO.
            print(items)


# creating a stack...
s = Stack()

print(s.isEmpty())
print(s.size())
print("")
s.push(4)
s.push("dog")
s.push(6)
s.push("bob")
print(s.isEmpty())
# s.printStack()

print("")
s.printStack()

print("")
print(s.isEmpty())
print(s.size())
print(s.pop())

print("")
print("")
s.printStack()
print("")
print(s.pop)
s.push("stash")
print(s.size())
s.printStack()

print("END.")
