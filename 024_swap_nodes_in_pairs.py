# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = prev = ListNode(-1)
        dummy.next = head

        while prev.next and prev.next.next:
            temp = prev.next.next.next
            prev.next.next.next = prev.next
            prev.next = prev.next.next
            prev.next.next.next = temp
            prev = prev.next.next
        return dummy.next


class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        prev = dummy = ListNode(-1)
        curt = dummy.next = head
        while curt and curt.next:
            next = curt.next
            temp = curt.next.next
            prev.next = next
            next.next = curt
            curt.next = temp

            prev = curt
            curt = temp
        return dummy.next


