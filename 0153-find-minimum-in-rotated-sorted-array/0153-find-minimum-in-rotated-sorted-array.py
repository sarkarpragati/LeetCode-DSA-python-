class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        
        if nums[low] <= nums[high]:
            return nums[low]
        
        while low <= high:
            mid = (low + high) // 2
            
           
            if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
           
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            
           
            if nums[mid] >= nums[low]:
                low = mid + 1
            
            else:
                high = mid - 1
                
        return -1
        