# https://leetcode.cn/problems/binary-tree-preorder-traversal/description/

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,2,3]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def pre(root):
            if root:
                output.append(root.val)
                pre(root.left)
                pre(root.right)
        
        pre(root)

        return output 
            


# iterative solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return [] 
        
        output = []
        stack = [root] 

        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return output 

# TODO: needs to revisit this iterative solution. 
# Had to draw recursion tree to see the solution.