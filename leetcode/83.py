from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        current = head
        while current.next != None:
            # compare current node with next node and remove duplicates
            if current.val == current.next.val:
                current.next = current.next.next
            # else move to next node
            else:
                current = current.next
        return head