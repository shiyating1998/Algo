class Solution:
    def fib(self, n: int) -> int:
        if n == 0 :
            return 0 
        if n == 1:
            return 1 
            
        dp = [0] * (n+1) 

        dp[1] = 1 

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# 1. Definition of the dp array, what each element represents
# 2. the formula to calculate each element
# 3. base case
# 4. initialize the dp array
# 5. the order of iteration
