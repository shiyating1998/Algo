# https://leetcode.cn/problems/combinations/description/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        result = []

        def backtracking(low, n, k):
            if len(path) == k:
                result.append(path[:])
                return 

            for i in range(low, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(i + 1, n, k)
                path.pop()

        backtracking(1,n,k)
        return result

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        low = 1 

        def backtracking(low, n, k):
            if low >= n - k + 2 or k <= 0:
                return []

            temp = []
            for i in range(low, n - k + 2):

                l = backtracking(i + 1, n, k - 1)

                if len(l) > 0:
                    for c in l:
                        c.append(i)
                        temp.append(c)
                else:
                    temp.append([i])
                
            return temp 

        return backtracking(low,n,k)