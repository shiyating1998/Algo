# refer: https://leetcode.com/problems/3sum/description/

# Method: sort the array first to avoid duplicate outputs
# fix the first element, and use two pointers to find the matching element, exit early, when no matching
# triplets is found 

# Time complexity: O(nlogn) for sorting, O(n^2) for looping? 
from typing import List 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  
            if i == 0 or nums[i-1]!=nums[i]:
                j = i + 1 
                z = len(nums) - 1 

                while j < z:
                    if nums[i] + nums[j] + nums[z] == 0:
                        output.append([nums[i], nums[j], nums[z]])
                        while j < z and nums[j] == nums[j+1]:
                            j += 1 
                        while z > j and nums[z-1] == nums[z]:
                            z -= 1 
                        j += 1 
                        z -= 1 
                    elif nums[i] + nums[j] + nums[z] < 0:
                        j += 1 
                    else:
                        z -= 1 

        return output


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,0,0,0]))