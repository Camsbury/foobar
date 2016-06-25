"""
Binary bunnies
==============

As more and more rabbits were rescued from Professor Booleans horrid
laboratory, you had to develop a system to track them,
since some habitually continue to gnaw on the heads of their brethren
and need extra supervision. For obvious reasons, you based your rabbit
survivor tracking system on a binary search tree, but all of a sudden
that decision has come back to haunt you.

To make your binary tree, the rabbits were sorted by their ages (in days)
and each, luckily enough, had a distinct age. For a given group,
the first rabbit became the root, and then the next one (taken in
order of rescue) was added, older ages to the left and younger to 
the right. The order that the rabbits returned to you determined
the end pattern of the tree, and herein lies the problem.

Some rabbits were rescued from multiple cages in a single rescue operation,
and you need to make sure that all of the modifications or pathogens
introduced by Professor Boolean are contained properly. Since the tree
did not preserve the order of rescue, it falls to you to figure out how
many different sequences of rabbits could have produced an identical tree
to your sample sequence, so you can keep all the rescued rabbits safe.

For example, if the rabbits were processed in order from [5, 9, 8, 2, 1],
it would result in a binary tree identical to one created from [5, 2, 9, 1, 8]. 

You must write a function answer(seq) that takes an array of up to 50
integers and returns a string representing the number (in base-10) of
sequences that would result in the same tree as the given sequence.

Attributes:
Binary search tree
Rabbits reverse sorted by ages
All have distinct ages


Test cases
==========

Inputs:
    (int list) seq = [5, 9, 8, 2, 1]
Output:
    (string) "6"

Inputs:
    (int list) seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Output:
    (string) "1"
"""

from math import factorial

def answer(seq):
    
    class Node:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.val = val
    
    class Tree:
        def __init__(self):
            self.root = None
            
        def add(self, val):
            if(self.root == None):
                self.root = Node(val)
            else:
                self._add(val, self.root)
    
        def _add(self, val, node):
            if(val < node.val):
                if node.right is not None:
                    self._add(val, node.right)
                else:
                    node.right = Node(val)
            else:
                if node.left is not None:
                    self._add(val, node.left)
                else:
                    node.left = Node(val)
        
        def pos(self):
            return self._pos(self.root)
        
        def _pos(self,node):
            
            if node.left is None:
                pos_left = 1
                num_left = 0
            elif self._num(node.left) == 1:
                pos_left = 1
                num_left = 1
            else:
                pos_left = self._pos(node.left)
                num_left = self._num(node.left)
                
            if node.right is None:
                pos_right = 1
                num_right = 0
            elif self._num(node.right) == 1:
                pos_right = 1
                num_right = 1
            else:
                pos_right = self._pos(node.right)
                num_right = self._num(node.right)
            
            return pos_left*pos_right*factorial(num_left
            +num_right)/(factorial(num_left)*factorial(num_right))
        
        def _num(self,node):
            count = 1
            if node.right is not None:
                count = count + self._num(node.right)
            if node.left is not None:
                count = count + self._num(node.left)
            return count
                    
    tree=Tree()
    for i in seq:
        tree.add(i)
    return tree.pos()