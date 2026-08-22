class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l,r =0,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r] , nums[l]
            r -=1
            l +=1
        l,r =0,k-1 # keep an eye k-1 
        while l<r:
            nums[l],nums[r] = nums[r] , nums[l]
            r -=1
            l +=1
        l,r =k,len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r] , nums[l]
            r -=1
            l +=1