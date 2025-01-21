class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        path = []
        result = []


        def h(s, startIndex, candidates, target):
            if s==target:
                result.append(path[:])
                return 
            
            for i in range(startIndex, len(candidates)):
                if candidates[i] + s > target:
                    break

                if i!=startIndex and candidates[i] == candidates[i-1]:
                    continue  
                
                s += candidates[i]
                path.append(candidates[i])
                h(s, i + 1, candidates, target)
                s -= candidates[i]
                path.pop()
        
        h(0,0,candidates,target)
        return result 