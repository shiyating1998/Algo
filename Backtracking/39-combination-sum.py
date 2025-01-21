class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        def h(s, startIndex, candidates, target):
            if s == target:
                result.append(path[:])
            
            for i in range(startIndex, len(candidates)):
                if s + candidates[i] > target:
                    continue 
                s += candidates[i]
                path.append(candidates[i])
                h(s, i, candidates, target)
                s -= candidates[i]
                path.pop()
            
        
        h(0,0,candidates,target)
        return result 

            
