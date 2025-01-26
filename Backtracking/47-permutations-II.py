class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        used = [0] * len(nums)


        def h (nums):
            used2 = defaultdict(int)
            if len(nums) == len(path):
                result.append(path[:])

            for i in range(len(nums)):
                if used2[nums[i]]:
                    continue 
                if used[i]:
                    continue 

                path.append(nums[i])
                used[i] = 1
                used2[nums[i]] = 1  
                h(nums)    
                used[i] = 0
                path.pop()
        h(nums)
        return result