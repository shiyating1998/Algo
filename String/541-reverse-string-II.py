# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Constraints:

# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104

class Solution:
    def reverse(self, s, begin, end):
        while begin < end:
            temp = s[begin]
            s[begin] = s[end]
            s[end] = temp
            begin += 1 
            end -= 1 
        # return s 
    def reverseStr(self, s: str, k: int) -> str:
        begin = 0 
        end = 2* k 

        s = list(s)
        c = len(s)
      
        while end < c:
            self.reverse(s,begin, begin + k - 1 )
            begin += 2*k
            end += 2*k 
            # print(s)
        
        if c - begin < k: 
            self.reverse(s,begin,c - 1)
        else:
            self.reverse(s,begin,begin + k - 1)
        
        return "".join(s)

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
assert Solution().reverseStr(s = "abcdefg", k = 2) == "bacdfeg"
# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"
assert Solution().reverseStr(s = "abcd", k = 2) == "bacd"