class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in range(len(nums)):
            count[nums[i]]=count.get(nums[i],0)+1
        heap=[]
        for num,freq in count.items():
            heapq.heappush(heap,(freq,num))
            if len(heap) >k:
                heapq.heappop(heap)
        return [item[1] for item in heap]