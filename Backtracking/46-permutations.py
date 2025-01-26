class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = defaultdict(int)

    
        def h(nums):
            if len(path) == len(nums):
                result.append(path[:])

            for i in range(len(nums)):
                if used[nums[i]]:
                    continue 
                
                path.append(nums[i])
                used[nums[i]] += 1 
                h(nums)
                used[nums[i]] -= 1
                path.pop()
        
        h(nums)
        return result 
