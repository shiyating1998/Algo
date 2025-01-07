# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# Time Complexity: O(nlogn)
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()

        num = nums[0]
        count = 0

        heap = []

        for n in nums:
            if n == num:
                count += 1
            else:
                heappush(heap, (-1 * count, num))
                count = 1
            num = n

        heappush(heap, (-1 * count, num))

        output = []
        for _ in range(k):
            output.append(heappop(heap)[1])

        return output

#Note: Use dictionary to find frequency
# 2) Use min heap to maintain a list of k elements, each sort only takes O(logk) time, and a total of O(nlogk) time. which is better than O(nlogn)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1 
        
        h = []
        for key,value in dic.items():            
            heappush(h,(value,key))
            if len(h) > k:
                heappop(h)
        output = []

        while h:
            output.append(heappop(h)[1])

        return output 
