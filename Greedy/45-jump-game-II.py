class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = 0
        steps = 0 
        cover = nums[0]

        if len(nums) > 1:
            while True: 
                steps += 1 
                if cover >= len(nums) - 1:
                    return steps 
                temp = cover 
                for i in range(cur, temp + 1):
                    cover = max(cover, nums[i] + i)
                cur = temp + 1
        return steps
        