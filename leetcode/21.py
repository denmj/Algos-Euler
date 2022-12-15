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

class SolutionTwo:
    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        if L1 is None:
            return L2
        if L2 is None:
            return L1
        if L1.val < L2.val:
            L1.next = self.mergeTwoLists(L1.next, L2)
            return L1
        else:
            L2.next = self.mergeTwoLists(L1, L2.next)
            return L2

class SolutionThree:
    def mergeTwoLists(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        while L1 and L2:
            if L1.val < L2.val:
                cur.next = L1
                L1 = L1.next
            else:
                cur.next = L2
                L2 = L2.next
            cur = cur.next
        if L1:
            cur.next = L1
        elif L2:
            cur.next = L2
             
        return res.next

list_one = ListNode(1, ListNode(2, ListNode(4, None)))
list_two = ListNode(9, ListNode(8, ListNode(6, None)))

print(Solution().mergeTwoLists(list_one, list_two))

