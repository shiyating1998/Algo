class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        
        output = -1
        g = 0
        for i in range(len(gas)):
            g += gas[i] - cost[i]
            if output == -1 and g >= 0:
                output = i 
            if g < 0: 
                output = - 1 
                g = 0  
        return output
        