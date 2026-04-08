import heapq
class kthLatgest:
    def find_kth_largest(self, num:list[int], k:int) -> int:
        min_heap = []
        for val in num:
            heapq.heappush(min_heap, val)
            if len(min_heap) > k:
                heapq.peappop(min_heap)
        return min_heap[0]


