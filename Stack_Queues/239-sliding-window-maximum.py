# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        output = []
        queue = deque()

        for i in range(len(nums)):
            num = nums[i]

            while len(queue)!= 0 and num > queue[-1]:
                queue.pop()

            queue.append(num)

            if i + 1 >= k:
                if i >= k and nums[i-k] == queue[0]:
                    queue.popleft()
                output.append(queue[0])
        
        return output 

#Note: 自己做出来的，还蛮有成就感的。手写了代码，然后仔细地做了运算，psuedocode的测试。 
# 学会了用deque()，是double ended queue,也就是双端队列，可以在两端进行插入和删除操作。