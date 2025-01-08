# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# # Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive solution
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        output = []

        def post(root):
            if root:
                post(root.left)
                post(root.right)
                output.append(root.val)
        
        post(root)
        return output 

# iterative solution, drew the recursion tree, pretty fun, need to revisit logic
class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                output.append(node)
            else:
                stack.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                # print(stack)
        return output 


# Iterative solution2, TODO revisit logic
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        output = []
        stack = [root]

        while stack:
            node = stack.pop()
            
            output.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            # print(stack)
        return output[::-1] 