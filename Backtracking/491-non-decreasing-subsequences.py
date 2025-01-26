class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = defaultdict(int)

        def h (startIndex, nums):
            if len(path) >= 2:
                result.append(path[:])
            used = defaultdict(int)
            for i in range(startIndex, len(nums)):
                if used[nums[i]] > 0:
                    continue
                # if i != startIndex and nums[i] == nums[i-1]:
                #     continue
                if len(path) == 0 or nums[i] >= path[-1]:
                    path.append(nums[i])
                    h(i+1,nums)
                    path.pop()
                    used[nums[i]] += 1 
                else:
                    continue 
        h(0,nums)
        return result 
                    
