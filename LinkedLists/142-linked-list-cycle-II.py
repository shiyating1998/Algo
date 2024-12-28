# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        fast = head 
        slow = head 

        while fast: 
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None 
            slow = slow.next 
            if fast == slow:
                break  
        
        output = head 
        while output != slow:
            output = output.next 
            slow = slow.next 

        return output


# x + y = A 
# x + y + n(y+z) = 2A 
# if n = 1:
#    x = z 
