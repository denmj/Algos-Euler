# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        currentNode = result
        temp_lists = []
        while head:
            temp_lists.append(head.val)
            head = head.next
        for i in temp_lists[::-1]:
            NewNode = ListNode(i)
            currentNode.next = NewNode
            currentNode = NewNode
        return result.next
