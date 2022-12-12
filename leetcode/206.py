# Definition for singly-linked list.
from typing import List, Optional
# from Patterns.linked_list.ll_0 import LinkedList

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

class SolutionTwoPointer:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

class SolutionRecursion:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)


# while l1:
#     print("Object: ", l1, "with: " ,l1.val)
#     l1 = l1.next

s = SolutionTwoPointer()
result = s.reverseList(l1)


while result:
    print("Object: ", result, "with: " ,result.val)
    result = result.next
