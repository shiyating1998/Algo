'''
https://leetcode.cn/problems/minimum-window-substring/description/
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.


Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
from cmath import inf
from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        needs = {}


        for c in t:
            if c in needs:
                needs[c] += 1
            else:
                needs[c] = 1

        valid = 0
        window = defaultdict(int)
        left = 0

        start = 0
        end = float(inf)

        for right in range(len(s)):

            if s[right] in needs:
                window[s[right]] += 1
                if window[s[right]] == needs[s[right]]:
                    valid += 1

            while valid == len(needs):
                if right - left < end - start:
                    end = right
                    start = left

                if s[left] in needs:
                    if window[s[left]] == needs[s[left]]:
                        valid -= 1
                    window[s[left]] -= 1
                left += 1
        if end == float(inf):
            return ""
        return s[start:end + 1]
s = "ADOBECODEBANC"
t = "ABC"
#Output: "BANC"

sol = Solution()
print(sol.minWindow(s,t))