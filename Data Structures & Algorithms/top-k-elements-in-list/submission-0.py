class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []

        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]= 1

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        for freq,num in heap:
            res.append(num)

        return res
        