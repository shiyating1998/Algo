# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def f(root):
            dp = [0,0]

            l = [0,0]

            r = [0,0]
            if root.left:
                l = f(root.left)
            if root.right:
                r = f(root.right)
            
            dp[0] = max(l[1],l[0]) + max(r[1],r[0])
            dp[1] = root.val + l[0] + r[0]
            return dp 
        
        return max(f(root))


        