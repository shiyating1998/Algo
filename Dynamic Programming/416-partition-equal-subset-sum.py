class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False 

        s = sum(nums) // 2
        dp = [0] * (s + 1)
        dp[0] = True 
        for num in nums:
            if num > s:
                return False 
            for i in range(s, num - 1, -1):                
                dp[i] = dp[i] or dp[i-num]
        
        return dp[-1] == True
# 值得表扬：遍历顺序思考的好
# base case， intiialization过了一遍psuedo code