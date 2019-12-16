Learn more or give us feedback
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
    def push(self, value):
        self.size += 1
        if self.size == 0:
            self.storage.add_to_head(value)
        else:
            return self.storage.add_to_tail(value)


    def pop(self):
        pass

    def len(self):
        pass