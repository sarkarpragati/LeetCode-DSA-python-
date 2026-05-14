class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices
        
        # Iterate twice to simulate circular behavior
        for i in range(2 * n):
            current_num = nums[i % n]
            
            # While stack is not empty and current num is greater than the element 
            # at the index stored at the top of the stack
            while stack and nums[stack[-1]] < current_num:
                index = stack.pop()
                res[index] = current_num
            
            # Only push indices during the first pass
            if i < n:
                stack.append(i)
                
        return res
        
        