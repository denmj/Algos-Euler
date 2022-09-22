"""
You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order, and each of their nodes contains a single digit.
  Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


lNode = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=0)))
lNode2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=0)))

print(lNode.val, lNode.next.val, lNode.next.next.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        while l1 != None:
            print(l1.val)

        return l1

s = Solution()
ll = s.addTwoNumbers(lNode, lNode2)