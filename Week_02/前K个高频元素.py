class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        import heapq
        heap = []
        result = []
        length = len(nums)
        if length<k:
            return []
        data_hash = Counter(nums)
        for key,v in data_hash.items():
            heapq.heappush(heap,(-v,key)) #堆排序 默认是最小堆，最大堆需要乘以 -1
        while k>0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
            print(k)
        return result