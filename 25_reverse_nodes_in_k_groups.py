# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head

        dummy = prev = ListNode(-1)
        dummy.next = head

        while True:
            tail = prev
            for _ in xrange(k):
                if tail.next:
                    tail = tail.next
                else:
                    return dummy.next
            temp = tail.next
            tail.next = None

            self.reverse(head)
            prev.next = tail
            head.next = temp
            prev = head
            head = temp

    def reverse(self, head):
        dummy = ListNode(-1)
        while head:
            temp = head.next
            head.next = dummy.next
            dummy.next = head
            head = temp
        return dummy.next


class Solution2:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if k <= 1:
            return head

        prev = dummy = ListNode(-1)
        curt = dummy.next = head

        while True:
            temp = curt
            for _ in range(k):
                if temp:
                    temp = temp.next
                else:
                    return dummy.next

            self.reverse(prev, curt, temp)
            prev = curt
            curt = temp
        return dummy.next

    def reverse(self, prev, curt, temp):
        # last node need to point to the temp
        tail = curt
        while curt is not temp:
            next = curt.next
            curt.next = prev.next
            prev.next = curt
            curt = next
        tail.next = temp