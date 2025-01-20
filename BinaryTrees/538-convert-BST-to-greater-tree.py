# https://leetcode.cn/problems/convert-bst-to-greater-tree/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def h(root, s):
            if root:
                if root.right:
                    s = h(root.right, s)
                
                root.val += s 
                s = root.val 
                if root.left:
                    s = h(root.left, s)
            return s 

        h(root,0)
        return root 