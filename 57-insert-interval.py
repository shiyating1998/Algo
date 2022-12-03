#ref: https://leetcode.com/problems/insert-interval/description/

# Time complexity: O(n), only needs to go through the array once
# Space complexity: O(n), just the output array

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        output = []

        for interval in intervals:
            # if the interval is not within the range of the newInterval, append
            # if the new interval has been already been appended, append 
            if not newInterval or interval[1]<newInterval[0]:
                output.append(interval)
            # here we encounter a place where the current interval is
            # in order with the newInterval to be inserted
            # append the interval in front, and set it to null 
            elif interval[0] > newInterval[1]:                
                output.append(newInterval)
                newInterval = None
                output.append(interval)
            # if the interval is in the range of the newInterval
            # update the range 
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        
        # if the interval is not yet appended, append to the end
        if newInterval:
            output.append(newInterval)
        return output 


            

