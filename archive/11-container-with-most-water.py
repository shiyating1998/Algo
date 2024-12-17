#refer: https://leetcode.com/problems/container-with-most-water/description/
from typing import List 

# Time complexity: O(n), use two pointers to traverse through the array from both ends

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        output = 0

        while left < right:
            h = min(height[left], height[right])
            output = max(output, h * (right - left))

            # since h of the area is determined by the min of the two,
            # move the smaller one of the two to maximize
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1 
        
        return output 

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([1,1]))