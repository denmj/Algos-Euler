"""
 Middle of the Linked List
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def middleNode(L: ListNode) -> ListNode:
        list_depth = 0
        list_val = []
        result = ListNode(0)
        currentNode = result

        while L:
            list_depth += 1
            list_val.append(L.val)
            L = L.next

        for i in list_val[len(list_val) // 2:]:
            NewNode = ListNode(i)
            currentNode.next = NewNode
            currentNode = NewNode

        return result.next

class SolutionTwoPointer:
    @staticmethod
    def middleNode(L: ListNode) -> ListNode:
        slow = fast = L
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
