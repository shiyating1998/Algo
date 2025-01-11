# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
 
# Follow up: Could you solve it both recursively and iteratively?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        output = True 
        if root:
            queue = deque([root])
            while queue:
                c = len(queue)
                level = []
                flag = True 
                for _ in range(c):
                    node = queue.popleft()
                    if node != 'N':
                        level.append(node.val)
                    
                        if node.left:
                            queue.append(node.left)
                        else:
                            queue.append('N')
                        if node.right:
                            queue.append(node.right)
                        else:
                            queue.append('N')
                        flag = False
                    
                    else:
                        level.append(node)
                        queue.append('N')
                        queue.append('N')
                if flag:
                    break 
                
                begin = 0
                end = len(level) - 1 
                while begin < end:
                    if level[begin] != level[end]:
                        return False 
                    begin += 1 
                    end -= 1 
        return output 

# Note: this approach compares the entire tree, O(2^h -1) where h is the height of the tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(root1, root2):
            if not root1 and not root2:
                return True 
            if not root1 or not root2:
                return False 
            
            if root1.val != root2.val:
                return False 
            
            return compare(root1.left, root2.right) and compare(root1.right, root2.left)
        
        return compare(root.left, root.right)

# recursive approach