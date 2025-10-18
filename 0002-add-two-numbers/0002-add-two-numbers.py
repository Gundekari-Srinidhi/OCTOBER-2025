# Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next
class Solution:
    def addTwoNumbers(self, l1:[list], l2:[list]):
        head=None
        temp=head
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            sum=val1+val2+carry
            carry=sum//10
            node=ListNode(sum % 10)
            if head is None:
                head=node
                temp=head
            else:
                temp.next=node
                temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return head
