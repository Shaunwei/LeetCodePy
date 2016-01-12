import heapq


class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or len(A) < k:
            return

        heap = []
        for a in A:
            if len(heap) == k:
                heapq.heappushpop(heap, a)
            else:
                heapq.heappush(heap, a)
        return heap[0]
