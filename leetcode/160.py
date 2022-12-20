from typing import List 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


# Using a dictionary / hash table
class SolutionThree:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        dictA = {}
        while headA:
            dictA[headA] = True
            headA = headA.next
        while headB:
            if headB in dictA:
                return headB
            headB = headB.next
        return None
