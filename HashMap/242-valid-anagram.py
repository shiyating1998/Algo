# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 
# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        arr = [0] * 26 

        for c in s:
            arr[ord(c)-ord('a')] += 1 
        for c in t:
            arr[ord(c)-ord('a')] -= 1 
        
        for c in arr:
            if c != 0:
                return False 
        
        return True 


# Note: don't need to remmeber the ASCII code for 'a', can calculate it directly by ord('a')