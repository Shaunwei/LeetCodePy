# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(-1)
        dummy.next = head

        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                val = prev.next.val
                while prev.next and prev.next.val == val:
                    prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next
