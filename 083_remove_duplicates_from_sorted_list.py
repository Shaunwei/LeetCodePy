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
        curt = head
        while curt and curt.next:
            while curt.next and curt.val == curt.next.val:
                curt.next = curt.next.next
            curt = curt.next
        return head


class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curt = head
        while curt and curt.next:
            if curt.val == curt.next.val:
                curt.next = curt.next.next
            else:
                curt = curt.next
        return head
