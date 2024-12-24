# https://leetcode.cn/problems/minimum-window-substring/description/
from collections import defaultdict


# Given two strings s and t of lengths m and n respectively, return the minimum window
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 


 

# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output_i = 0
        output_j = len(s) + 1
        dict = defaultdict(int)
        if len(t) > len(s):
            return ""
        else:
            # initialize dict
            for a in t:
                dict[a] += 1
            print(dict)

            count = len(t)
            i = 0
            j = 0
            while j < len(s):
                dict[s[j]] -= 1
                if dict[s[j]] >= 0:
                    count -= 1

                while count == 0:
                    if (output_j - output_i) > j - i:
                        output_j = j
                        output_i = i 
                    
                    dict[s[i]] += 1
                    if dict[s[i]] > 0:
                        count += 1
                    i += 1

                j += 1

            if output_j == len(s) + 1:
                # not Found
                return ""
            else:
                return s[output_i:output_j+1]



# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
assert Solution().minWindow(s = "ADOBECODEBANC", t = "ABC") == "BANC"

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
assert Solution().minWindow(s = "a", t = "a") == "a"

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
assert Solution().minWindow(s = "a", t = "aa") == ""

s = "acbbbaca"
t = "bb"
assert Solution().minWindow(s = s, t = t) == "bb"

s = "acbabaaaaacbaca"
t = "bb"
print(Solution().minWindow(s = s, t = t))
assert  Solution().minWindow(s = s, t = t) == "bab"

s = "acbabaaaaacbaca"
t = "bbz"
print(Solution().minWindow(s = s, t = t))
assert  Solution().minWindow(s = s, t = t) == ""
