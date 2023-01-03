# question: https://leetcode.com/problems/product-of-array-except-self/description/
# refer: https://leetcode.com/problems/product-of-array-except-self/solutions/65622/simple-java-solution-in-o-n-without-extra-space/

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Brute force
        # for ever number, multiply to the rest of the array
        # O(n^2)
        # output = [1] * len(nums)

        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             output[j] *= nums[i]
        # return output

        # O(n) Solution
        
        output = [1] * len(nums)
        # multiply the numbers on the left, incrementally, from front to back
        # [1, 2, 3, 4]
        # [x, 1, 1*2, 1*2*3]
        for i in range(1, len(nums)):        
            output[i] = output[i-1] * nums[i-1]

        # multiply the numbers on the right, incrementally, from back to front 
        # [1, 2, 3, 4]
        # [2*3*4, 3*4, 4, x]
        right = 1 
        for j in range(len(nums)-2, -1, -1):
            right *= nums[j+1]
            output[j] = output[j] * right

        return output  

s = Solution()

print(s.productExceptSelf([1,2,3,4]))
print(s.productExceptSelf([-1,1,0,-3,3]))