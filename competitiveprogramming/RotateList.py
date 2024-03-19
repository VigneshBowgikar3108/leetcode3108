# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        l=1
        curr = head
        while curr.next:
            curr=curr.next
            l+=1
        curr.next=head
        k=k % l
        rotate=l-k
        while rotate:
            curr=curr.next
            rotate-=1
        head=curr.next
        curr.next=None
        return head