# https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

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

# Recursive 
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def inorder(root):
            if root: 
                inorder(root.left)
                output.append(root.val)
                inorder(root.right)
        
        inorder(root)
        return output 


# Iterative: drew the recursion tree, TODO, needs to revisit the logic, really learned how to use stack to solve recurison problems, pretty fun 
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            if isinstance(node,int):
                output.append(node)
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(node.val)
                if node.left:
                    stack.append(node.left)
        
        return output 