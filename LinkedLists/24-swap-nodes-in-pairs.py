# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Explanation:



# Example 2:
# Input: head = []
# Output: []

# Example 3:
# Input: head = [1]
# Output: [1]

# Example 4:
# Input: head = [1,2,3]
# Output: [2,1,3]

 

# Constraints:

# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        pre = dummy 
        cur = head 

        while cur:
            after = cur.next  
            if after:
                pre.next = after 
                temp = after.next
                after.next = cur 
                cur.next = temp 
                pre = cur 
                cur = temp 
            else:
                cur = cur.next 
        return dummy.next 
    

# Note: 最常用的情况没有测啊，测试不完整不够仔细。耐心冷静一步一步写出来。