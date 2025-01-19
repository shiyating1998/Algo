# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

 

# Example 1:
# Input: nums= [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # [low, high)
        def h(nums, low, high):
            if high - low == 0 :
                return None 
        
            if high - low == 1:
                return TreeNode(nums[low])
            
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = h(nums, low , mid )
            root.right = h(nums, mid + 1, high)
            
            return root 

        return h(nums,0,len(nums)) 

class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 :
            return None 
        
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        # [low, high]
        def h(low, high):

            
            if low <= high:
                mid = (low+high) // 2
        return root        
        