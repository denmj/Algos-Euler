from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # 1. Find the length of the list
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        # 2. Find the kth node from the beginning
        node = head
        for i in range(k - 1):
            node = node.next
        kth_from_beginning = node
        # 3. Find the kth node from the end
        node = head
        for i in range(length - k):
            node = node.next
        kth_from_end = node
        # 4. Swap the values
        kth_from_beginning.val, kth_from_end.val = kth_from_end.val, kth_from_beginning.val
        return head

h = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
s.swapNodes(h, 2)

