class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        output = [0]*len(nums)


        for i in range(len(nums) - 1,  -1 , -1):
            if nums[i] > len(nums) - i - 2:
                output[i] = 1 

            if output[i] != 1:
                for j in range(1, nums[i] + 1):
                    if i + j >= len(nums):
                        break
                    if output[j + i] == 1:
                        output[i] = 1
                        break
        # print(output)
        return output[0] == 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = nums[0]

        for i in range(1, len(nums)):
            if i <= cover: 
                cover = max(cover, nums[i] + i)

        return cover >= len(nums) - 1 


# Note: did well on trying the edge cases, especially when array length is 1 and value =0 should return True 

# Greedy algorithm on "cover" needs to be learned.