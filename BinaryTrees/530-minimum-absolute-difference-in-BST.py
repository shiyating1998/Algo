# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/ 530-minimum-absolute-difference-in-BST.py
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

# Example 1:
# Input: root = [4,2,6,1,3]
# Output: 1

# Example 2:
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [2, 104].
# 0 <= Node.val <= 105
 

# Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def __init__(self):
        self.diff = 10000000
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if root:
            if root.left:
                if root.val - root.left.val < self.diff:
                    self.diff = root.val - root.left.val 
                self.getMinimumDifference(root.left)
            if root.right:
                if root.right.val - root.val < self.diff:
                    self.diff = root.right.val - root.val 
                self.getMinimumDifference(root.right)
        return self.diff    

class Solution:
    def __init__(self):
        self.diff = 10000000
        self.pre = None 
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        if root:
            self.getMinimumDifference(root.left)
            if self.pre != None:
                self.diff = min(root.val - self.pre.val, self.diff)
            self.pre = root
            self.getMinimumDifference(root.right)
        return self.diff  

# Note: track the previous node, this is inorder traversal