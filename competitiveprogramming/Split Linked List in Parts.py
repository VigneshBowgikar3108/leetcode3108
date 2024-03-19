# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans=[]
        temp=head
        n=0
        while temp:
            n+=1
            temp=temp.next
        a,b=divmod(n,k)
        temp=head
        prev=None
        for i in range(k):
            ans.append(temp)
            for j in range(a):
                if temp :
                    prev=temp
                    temp=temp.next
            if b and temp:
                prev=temp
                temp=temp.next
                b-=1

            if prev:
                prev.next=None
        return ans       
        