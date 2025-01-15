# https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/
# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [1,null,2,2]
# Output: [2]
# Example 2:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
 

# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.mode = 0 
        self.output = []
        self.num = None 
        self.count = 0 
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            self.findMode(root.left)
            if self.num == None: #Note: if we use 'not self.num' will have error if num==0, so it should check whether self.num is None or not...
                self.num = root.val 
                self.count = 1 
                self.mode = 1 
                self.output = [root.val]
            else:
                if self.num == root.val:
                    self.count += 1 
                else:
                    self.count = 1 
                    self.num = root.val 
                
                if self.count > self.mode:
                    self.mode = self.count 
                    self.output = [root.val]
                elif self.count == self.mode:
                    self.output.append(root.val)
            self.findMode(root.right)
        return self.output 

    