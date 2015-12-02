__author__ = 'shawei'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(-1)
        MAX_INT = 2 ** 31 - 1
        while l1 or l2:
            v1 = l1.val if l1 else MAX_INT
            v2 = l2.val if l2 else MAX_INT
            if v1 > v2:
                prev.next = l2
                l2 = l2.next
            else:
                prev.next = l1
                l1 = l1.next
            prev = prev.next
        return dummy.next


class Solution2:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        curt = dummy = ListNode(-1)

        while l1 and l2:
            if l1.val <= l2.val:
                curt.next = l1
                l1 = l1.next
            else:
                curt.next = l2
                l2 = l2.next
            curt = curt.next

        if l1:
            curt.next = l1
        if l2:
            curt.next = l2
        return dummy.next
