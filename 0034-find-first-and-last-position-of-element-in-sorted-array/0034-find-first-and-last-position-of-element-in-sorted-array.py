class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def LowerBound(arry,target):
            low, high = 0, len(nums) - 1
            lb = -1
            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target:
                    lb = mid 
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return lb

        def HigherBound(nums, target):
            low, high = 0, len(nums) - 1
            hb = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    hb = mid
                    low = mid + 1   
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return hb
        return [LowerBound(nums, target), HigherBound(nums, target)]
      