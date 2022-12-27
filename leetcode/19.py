from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return None
        p = head
        q = head
        for i in range(n):
            q = q.next
        if q is None:
            return head.next
        while q.next is not None:
            p = p.next
            q = q.next
        p.next = p.next.next
        return head


class SolutionTwo:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        list_len = 0
        while cur is not None:
            list_len += 1
            cur = cur.next
        
        if list_len == 1:
            return None
        
        if list_len == n:
            return head.next

        cur = head
        for i in range(list_len - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head

# check the result
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

s = SolutionTwo()
l = s.removeNthFromEnd(l, 2)