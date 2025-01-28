class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        sign = 0 # 0 - not set, 1 - positive, 2 - negative 

        if len(nums) == 1:
            return 1 
        
        i = 1 
        count = 1
        num = nums[0] 
        while i < len(nums):
            if num < nums[i]:
                if sign==0 or sign==2:
                    count += 1 
                    num = nums[i]
                    sign = 1 
                else:
                    num = max(num, nums[i])
            elif num > nums[i]:
                if sign==0 or sign==1:
                    count += 1 
                    num = nums[i]
                    sign = 2 
                else:
                    num = min(num, nums[i])
            #elif num == nums[i]:
            i += 1 
                

        return count