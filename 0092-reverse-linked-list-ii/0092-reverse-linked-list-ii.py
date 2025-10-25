# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        temp=head
        count=1
        prev=None
        while count<left:
            prev=temp
            temp=temp.next
            count+=1
        start=temp
        end_prev=prev
        while temp and count<=right:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
            count+=1
        if end_prev:
            end_prev.next=prev
        else:
            head=prev
        start.next=temp
        return head
        