# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        heap = [(node.val, node) for node in lists if node]
        heapq.heapify(heap)

        dummy = prev = ListNode(-1)
        while heap:
            _, node = heapq.heappop(heap)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next


class Solution2:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if not lists:
            return

        # min heap
        head_list = []

        for head in lists:
            if head:
                heapq.heappush(head_list, [head.val, head])

        curt = dummy = ListNode(-1)
        while head_list:
            _, head = heapq.heappop(head_list)
            curt.next = head
            curt = curt.next
            if head.next:
                heapq.heappush(head_list, [head.next.val, head.next])
        return dummy.next