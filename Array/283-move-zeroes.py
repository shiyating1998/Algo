# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.


 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = 0
        write = 0
        while read < len(nums):
            if (nums[read]!=0):
                nums[write] = nums[read]
                write +=1
            read += 1 
        
        while write < len(nums):
            nums[write] = 0
            write += 1  

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
assert Solution().moveZeroes(nums = [0,1,0,3,12]) == [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
assert Solution().moveZeroes(nums = [0]) == [0]

# Note: needs to trace through the code after coding, at least go through the examples and couple edge cases

# Time Complexity: O(n)
# Space Complexity: O(1)


# 第二种解法的本质是一个循环不变量：在每一次循环前，j 的左边全部都是不等于0的

# 起始j为0，明显满足
# 此后每一次循环中，若nums[i] = 0，则j保持不变，满足；若nums[i] != 0，交换后j增一，仍然满足
# 这就保证了最后结果的正确性。
public void moveZeroes(int[] nums)  {
    int length;
    if (nums == null || (length = nums.length) == 0) {
        return;
    }
    int j = 0;
    for (int i = 0; i < length; i++) {
        if (nums[i] != 0) {
            if (i > j) {// #1
                nums[j] = nums[i];
                nums[i] = 0;
            }
            j++;
        }
    }
}