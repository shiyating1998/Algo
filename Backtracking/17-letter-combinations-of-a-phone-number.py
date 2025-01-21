# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Input: digits, string
        # output: list of strings
        # Cases:
        # 1) digits empty: return []
        # 2) len(digits)==1: return all possible char
        # 3) 234 ad ae af -> adg adh adi ...

        # Psuedo code:
        # path = []
        # result = []
        # 
        # startIndex = 0 
            # if len(path) == len(digits):
            #   result.append(path[:])
            #   return 
            # for each letter in digit:
                # path.append(letter)
                # backtrack(startindex + 1, digits)
                # path.pop()
        
        if len(digits) == 0:
            return []
        path = []
        result = []
        startIndex = 0

        dic = {}
        dic["2"] = "abc"
        dic["3"] = "def"
        dic["4"] = "ghi"
        dic["5"] = "jkl"
        dic["6"] = "mno"
        dic["7"] = "pqrs"
        dic["8"] = "tuv"
        dic["9"] = "wxyz"
        def h(startIndex, digits):
            if len(path) == len(digits):
                result.append("".join(path))
                return 
            for letter in dic[digits[startIndex]]:
                path.append(letter)
                h(startIndex + 1, digits)
                path.pop()
        
        h(startIndex, digits)
        return result 

# 时间复杂度: O(3^m * 4^n)，其中 m 是对应三个字母的数字个数，n 是对应四个字母的数字个数
# 空间复杂度: O(3^m * 4^n)