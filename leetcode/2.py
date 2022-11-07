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


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        result = ListNode(0)
        current_node = result

        while l1 or l2 or carry != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            print(val1, "+", val2, '=', val1 + val2 + carry, '*******', 'carry: ', (val1 + val2 + carry) // 10,
                  'remainder: ', (val1 + val2 + carry) % 10)
            sum_ = (val1 + val2 + carry)
            print(sum_)
            carry = sum_ // 10
            print(carry)
            remainder = sum_ % 10
            print(remainder)
            Node = ListNode(remainder)
            current_node.next = Node
            current_node = Node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next


lNode = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=0)))
lNode2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=0)))

s = Solution()
resultNode = s.addTwoNumbers(lNode, lNode2)

print(resultNode.val)

