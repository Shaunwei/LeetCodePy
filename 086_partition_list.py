# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        less = lptr = ListNode(-1)
        greater = gptr = ListNode(-1)

        while head:
            if head.val < x:
                lptr.next = head
                lptr = lptr.next
            else:
                gptr.next = head
                gptr = gptr.next
            head = head.next
        gptr.next = None
        lptr.next = greater.next
        return less.next
