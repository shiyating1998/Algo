'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.



Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.


Follow up: Can you solve it in O(n) time and O(1) space?
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        r1 = len(s) - 1
        r2 = len(t) - 1

        c1 = 0
        c2 = 0
        while r1 != 0 and r2 != 0:
            if s[r1] == '#':
                c1 += 1
                r1 -= 1
            if t[r2] == '#':
                c2 += 1
                r2 -= 1


            if s[r1] != t[r2]:

                #else:
                    if c1 > 0:
                        r1 -= 1
                        c1 -= 1
                    elif c2 > 0:
                        r2 -= 1
                        c2 -= 1
                    else:
                        return False
            else:
                r1 -= 1
                r2 -= 1
        return r1 == r2

sol = Solution()
s = "a#c"
t = "b"

s = "ab##"
t = "c#d#"
print(sol.backspaceCompare(s,t))

#TODO 