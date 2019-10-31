# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:56:39 2018

@author: Leon
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    '''
    Time Limit Exceeded
    '''
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

class Solution2:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        temp = root
        while temp != None:
            height += 1
            temp = temp.left
        return self.count(root, height)
            
    def count(self, root, maxHeight):
        if root is None:
            return 0
        if root.left is None:
            return 1
        height = 0
        temp = root.left
        while temp != None:
            height += 1
            temp = temp.right
        if height == (maxHeight - 1):# left tree is perfect at the lowest level
            return pow(2, height) + self.count(root.right, maxHeight - 1)
        else:# right tree must be perfect at one level shallower
            return pow(2, height) + self.count(root.left, maxHeight - 1)