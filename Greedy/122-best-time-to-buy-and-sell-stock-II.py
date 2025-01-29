class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        cur = prices[0]
        if len(prices) > 1:
            for i in range(1 , len(prices)):
                if prices[i] > cur: 
                    profit += prices[i] - cur 
                
                cur = prices[i]
        
        return profit