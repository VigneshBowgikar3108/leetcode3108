# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        left = head
        right = head
        count = 0
        
        while count < k - 1:
            right = right.next
            count += 1
        
        initial_right = right
        
        while right.next is not None:
            left = left.next
            right = right.next
        
        left.val, initial_right.val = initial_right.val, left.val
        return head
