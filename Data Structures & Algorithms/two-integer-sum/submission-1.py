class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq ={}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in freq:
                return [freq[val],i]
            else:
                freq[nums[i]]=i


