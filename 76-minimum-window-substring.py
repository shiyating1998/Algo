
# Question: https://leetcode.com/problems/minimum-window-substring/description/
# Time complexity: O(n + m), iterate through t once for counttable, and s once for finding the min substring 
# Space complexity: countTable O(s) for count of each letter in the window 

from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        if len(s) < len(t):
            return ""

        countTable = defaultdict(int)        
        for c in t:
            countTable[c] += 1       

        start = 0
        end = 0
        output = ""

        while end < len(s):
            c = s[end]
            end += 1 
            countTable[c] -= 1 
            # find the substring with the min length, note here it is <= not == 
            if max(countTable.values()) <= 0:
                while countTable[s[start]] != 0:
                    countTable[s[start]] += 1 
                    start += 1                     
                if output == "":
                    output = s[start:end]
                elif len(output) > end - start:                   
                    output = s[start:end]
                
        return output 

s = Solution()
print(s.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(s.minWindow(s = "a", t = "a"))
print(s.minWindow(s = "a", t = "aa"))
print(s.minWindow(s = "acbbaca", t = "aba")) ## case that failed in the first try