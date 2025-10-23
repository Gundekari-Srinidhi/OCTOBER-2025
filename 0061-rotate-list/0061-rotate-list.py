class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = head  
        pos = k % length
        if pos == 0:
            tail.next = None  
            return head
        flag = head
        for i in range(length - pos - 1):
            flag = flag.next
        new_head = flag.next
        flag.next = None

        return new_head
