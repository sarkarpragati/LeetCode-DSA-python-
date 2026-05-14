class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        greater_map = {}
        stack = []

        for num in nums2:
            # If the current number is larger than the number on top of the stack,
            # it means we've found the 'next greater' for that stack element.
            while stack and num > stack[-1]:
                smaller_val = stack.pop()
                greater_map[smaller_val] = num
            
            stack.append(num)

        # Step 2: Construct the result for nums1 using the map.
        # .get(n, -1) handles cases where no greater element was ever found.
        return [greater_map.get(n, -1) for n in nums1]
        
        