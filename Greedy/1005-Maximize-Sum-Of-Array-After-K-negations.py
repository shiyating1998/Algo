class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()

        s = 0

        m = 1000
        for num in nums:
            if num < 0 and k > 0:
                s += -num 
                m = min(-num, m)
                k -= 1 
            elif num >= 0 and k > 0:
                s += num 
                m = min(num,m)
            else:
                s += num 
        
        if k > 0:
            s -= m
            if k%2==0: 
                s += m
            else:
                s -= m

        return s  

                
