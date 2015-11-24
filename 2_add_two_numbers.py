__author__ = 'shawei'
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        4: 20 - 4: 27
        """
        # two pointer
        # additional carry

        dummy = prev = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = (v1 + v2 + carry)
            carry = val / 10
            prev.next = ListNode(val % 10)

            prev = prev.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        return dummy.next
