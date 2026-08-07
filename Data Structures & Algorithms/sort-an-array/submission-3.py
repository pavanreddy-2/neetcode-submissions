class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #merge sort
        def merge_sort(nums):
            if len(nums)<= 1:
                return nums
            mid = len(nums)//2
            left = merge_sort(nums[:mid])
            right =merge_sort(nums[mid:])
            result =[]
            i=j=0
            while i<len(left) and j <len(right):
                if left[i]<right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])

            return result
        return merge_sort(nums)

        #---------------qucik sort -------------

        # def partion(arr,low,high):
        #     pivot = arr[high]
        #     i = low-1

        #     for j in range(low,high):
        #         if arr[j] <= pivot:
        #             i+=1
        #             arr[i],arr[j]=arr[j],arr[i]
        #     arr[i+1],arr[high] = arr[high],arr[i+1]

        #     return i+1
        # def quick_sort(arr,low,high):
        #     if low<high:
        #         pi = partion(arr,low,high)
        #         #sorting the left and right
        #         quick_sort(arr,low,pi-1)
        #         quick_sort(arr,pi+1,high)
        # quick_sort(nums,0,len(nums)-1)
        # return nums
