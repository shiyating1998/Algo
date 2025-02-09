class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones) // 2

        dp = [0] * (s + 1)

        dp[0] = 0 
        m = 0

        for stone in stones:
            if stone > s:
                continue 
            for i in range(s, stone - 1 , -1):
                dp[i] = max(dp[i], dp[i - stone] + stone)
        print(dp)
        return sum(stones) - dp[-1] - dp[-1]

# be careful of what needs to be returned...
# also the initialization of the dp array, the size of the dp array 
