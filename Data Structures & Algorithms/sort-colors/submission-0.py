class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts=[ 0 for _ in range(3)]
        for i in range(len(nums)):
            index=nums[i]
            counts[index] +=1
        i=0
        for index in range(len(counts)):
            for j in range(counts[index]):
                nums[i]= index
                i +=1
            




        