class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left =1
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]: #current element must comapre withh previous element nott withh the left elementt
                nums[left] =nums[right]
                left +=1
        
        return left
        