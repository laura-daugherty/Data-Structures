import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
# Code Along
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
    
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

# Laura's solution
        # newTree = BinarySearchTree(value)
        # if self is None:
        #     self = newTree
        # else:
        #     if newTree.value < self.value:
        #         if self.left is None:
        #             self.left = newTree
        #         else:
        #             self.left.insert(newTree.value)
        #     else:
        #         if self.right is None:
        #             self.right = newTree
        #         else:
        #             self.right.insert(newTree.value)


        # < go left
        # >= go right
        # print("self.right.value", self.right.value)
        # print("self.left.value", self.left.value)




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)


            #To search a given key in Binary Search Tree, we first compare it with root, 
        # if the key is present at root, we return root. If key is greater than root's key, 
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
# code along




#Laura's progress
        # if self.value == target:
        #     return True
        # if target < self.value:
        #     self.left.contains(target)
        # if target >= self.value:
        #     self.right.contains(target)
        # else:
        #     return False


    # Return the maximum value found in the tree
    def get_max(self):
        # Go right until you can go right no further
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every node exactly one time
        # go left until you can't anymore, then
        # go back and go right
        # in here somewhere, you want to call cb(node)
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
