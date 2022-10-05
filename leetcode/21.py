from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        l1_temp = []
        l2_temp = []
        result = ListNode(0)
        currentNode = result

        while L1:
            l1_temp.append(L1.val)
            L1 = L1.next

        while L2:
            l2_temp.append(L2.val)
            L2 = L2.next
        for val in sorted(l1_temp + l2_temp):
            newNode = ListNode(val)
            currentNode.next = newNode
            currentNode = newNode
        return result.next


list_one = ListNode(1, ListNode(2, ListNode(4, None)))
list_two = ListNode(9, ListNode(8, ListNode(6, None)))

print(Solution().mergeTwoLists(list_one, list_two))

