class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output = nums[0]
        s = nums[0] 
        if len(nums) != 1:
            for i in range(1, len(nums)):
                if s < 0: 
                    s = nums[i]
                    output = max(s, output)
                elif s >= 0 and s + nums[i] < 0:
                    s = 0
                elif s >= 0:
                    s += nums[i]
                    output = max(s, output)
                    
        return output