# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 
# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# # ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        if len(r) > len(m):
            return False 
        
        arr = [0] * 26 

        for a in r:
            arr[ord(a)-ord('a')] += 1 
        
        for b in m:
            arr[ord(b)-ord('a')] -= 1 
        
        for c in arr:
            if c > 0:
                return False 
        
        return True 
