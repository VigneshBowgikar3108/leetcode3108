# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        dummy=headnew=ListNode(None,head)
        curr=head
        while curr:
            while a and a[-1].val<curr.val:
                a.pop()
            a.append(curr)
            curr=curr.next
        for i in a:
            headnew.next=i
            headnew=headnew.next
        return dummy.next
                
                
                


        