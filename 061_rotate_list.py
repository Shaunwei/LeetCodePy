# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head

        tail = head
        length = 1
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        tail.next = head
        for _ in range(length - k):
            tail = tail.next
        head = tail.next
        tail.next = None
        return head

