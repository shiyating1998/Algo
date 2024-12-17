
'''
For those who got confused by if the last solution is O(n^2) or O(n), please take a close look at the entering of the logic: if(!num_set.contains(num-1)).
That means, for example, 6,5,4,3,2,1 input, only the value 1 is valid for the loop(all other values have its value - 1 in the set), that is O(n).
Another corner example, 2, 5, 6, 7, 9, 11. All of these numbers are the "entrance" for the logic but the while loop doesn't run much. That is O(n) as well.
'''
# Question: https://leetcode.com/problems/longest-consecutive-sequence/
# Refer: https://leetcode.com/problems/longest-consecutive-sequence/solutions/127576/longest-consecutive-sequence/


# Naive solution: sort the array and iterate O(nlogn) 
# O(n) solution, trade space for time. Use a set to keep track of the 
# elements, then iterate through the elements, to find the "starting element" of the sequence
# and count the maxLen of the sequence 
# Space complexity: O(n)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        # add the num to the set 
        s = set()
        for num in nums:
            s.add(num)
        # for each num in the set
        for num in s: 
            # if it is not the "starting element", continue 
            if num - 1 in s:
                continue
            
            # find the len of the sequence
            curNum = num
            curLen = 1 
            # print(curNum)
            while (curNum + 1) in s:
                curNum += 1 
                curLen += 1

            # update output 
            output = max(output,curLen)
        
        return output 

s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))