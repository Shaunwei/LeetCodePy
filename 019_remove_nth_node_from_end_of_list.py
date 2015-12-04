# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        4:03 - 4: 08
        """
        # slow fast pointer
        # how fast start, dummy
        if not head or not n:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        fast = dummy
        for _ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(-1)
        dummy.next = head

        tail = dummy
        for _ in xrange(n):
            if tail:
                tail = tail.next
            else:
                return dummy.next

        while tail.next:
            tail = tail.next
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
