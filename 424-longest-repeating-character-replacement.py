# question: https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Time Complexity: O(n)

# keep a sliding window, where the window length is valid, if the number of unmatching char 
# is less than k (that is, find the length - maxFreq char )
# shrink the window if it is not valid, and increase the window size if it is valid 

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        maxF = 1
        output = 0

        left = 0
        right = 0

        while right < len(s):
            window[s[right]] += 1 
            maxF = max(maxF, window[s[right]])
            right += 1 

            if k - (right - left - maxF) >= 0:
                output = max(output, right - left)
                
            else:
                window[s[left]] -= 1 
                left += 1  

        return output 

s = Solution()
print(s.characterReplacement("ABAB", k = 2))
print(s.characterReplacement(s = "AABABBA", k = 1))