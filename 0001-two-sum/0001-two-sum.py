class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range (len(nums)):
            remainder = target - nums[i]
            if remainder in dict:
                return [dict[remainder],i]
            dict[nums[i]] = i
        