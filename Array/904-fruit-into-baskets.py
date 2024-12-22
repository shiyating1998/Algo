# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.

# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.

# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

# Given the integer array fruits, return the maximum number of fruits you can pick.

# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

from typing import List


class Solution2:
    def totalFruit(self, fruits: List[int]) -> int:
        l = len(fruits)
        output = 2
        if l == 1 or l == 2:
            return l
        else:
            i = 0
            j = 2
            i_val = fruits[0]
            j_val = -1
            if fruits[1] != i_val:
                j_val = fruits[1]
            while j < len(fruits):
                if i_val == fruits[j] or j_val == fruits[j]:
                    output = max(output, j - i + 1)
                else:
                    if j_val == -1:
                        j_val = fruits[j]
                        output = max(output, j - i + 1)
                    else:
                        c = j - 1
                        if i_val == fruits[c]:
                            while fruits[c] != j_val:
                                c -= 1
                            j_val = fruits[j]
                            i = c + 1
                        else:
                            while fruits[c] != i_val:
                                c -= 1
                            i_val = fruits[j]
                            i = c + 1
                j += 1
            return output

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int) 
        output = 0
        i = 0
        j = 0
        c = 0

        while j < len(fruits):
            if dic[fruits[j]] == 0:
                c += 1
            dic[fruits[j]] += 1
            while c > 2:
                dic[fruits[i]] -= 1
                if dic[fruits[i]] == 0:
                    c -= 1
                i += 1 
            output = max(output, j - i + 1)
            j += 1

        return output


# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
assert Solution().totalFruit([1, 2, 1]) == 3

# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
assert Solution().totalFruit([0, 1, 2, 2]) == 3

# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
assert Solution().totalFruit([1, 2, 3, 2, 2]) == 4

fruits = [1]
assert Solution().totalFruit(fruits) == 1

fruits = [0, 1]
assert Solution().totalFruit(fruits) == 2

fruits = [0, 1, 2]
assert Solution().totalFruit(fruits) == 2

fruits = [1, 1]
assert Solution().totalFruit(fruits) == 2

fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
assert Solution().totalFruit(fruits) == 5

# Note it is very important to see how the windows should be shrinking, the conditions, in this case, we shrink in
# such a way that the value of one of the basket totally away

fruits = [0, 0, 1, 1]
assert Solution().totalFruit(fruits) == 4

fruits = [3, 3, 3, 1, 4]
assert Solution().totalFruit(fruits) == 4

fruits = [1, 1, 6, 5, 6, 6, 1, 1, 1, 1]
assert Solution().totalFruit(fruits) == 6
