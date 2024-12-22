# https://leetcode.cn/problems/backspace-string-compare/description/
# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
 

# Follow up: Can you solve it in O(n) time and O(1) space?

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_end = len(s) - 1
        t_end = len(t) - 1
        c1 = 0  
        c2 = 0  
        while s_end >= 0 and t_end >= 0:
            if s[s_end] != '#' and t[t_end] != '#':
                if c1 > 0:
                    s_end -= 1
                    c1 -= 1
                elif c2 > 0:
                    t_end -= 1
                    c2 -= 1
                else:
                    if s[s_end] != t[t_end]:
                        return False
                    s_end -= 1
                    t_end -= 1
            elif s[s_end] == '#':
                c1 += 1
                s_end -= 1
            elif t[t_end] == '#':
                c2 += 1
                t_end -= 1
        
        while t_end >= 0:
            if t[t_end] == '#':
                c2 += 1 
                t_end -= 1
            else:
                if c2 > 0:
                    t_end -= 1
                    c2 -= 1
                else:
                    return False
        while s_end >= 0:
            if s[s_end] == '#':
                c1 += 1 
                s_end -= 1
            else:
                if c1 > 0:
                    s_end -= 1
                    c1 -= 1
                else:
                    return False
        return True
# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
assert Solution().backspaceCompare("ab#c","ad#c") == True 

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
assert Solution().backspaceCompare("ab##","c#d#") == True

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
assert Solution().backspaceCompare("a#c","b") == False

s ="bxj##tw"
t ="bxj###tw"
assert Solution().backspaceCompare(s,t) == False