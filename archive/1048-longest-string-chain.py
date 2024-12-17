# leetcode problem 1048
# https://leetcode.com/problems/longest-string-chain/description/

from collections import defaultdict
class Solution:
    def longestStrChain(self, words) -> int:
        table = defaultdict(int)

        for word in sorted(words,key=len):
            for i in range(len(word)):    
                table[word] = max(table[word], table[word[:i]+word[i+1:]]+1)
        return max(table.values())

