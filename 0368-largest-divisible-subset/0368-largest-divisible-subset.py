class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
        # dp[i] will store the size of the largest divisible subset ending at nums[i]
        dp = [1] * n
        # parent[i] will store the index of the previous element in the subset
        parent = [-1] * n
        
        max_size = 0
        max_idx = 0
        
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            # Keep track of the overall largest subset found
            if dp[i] > max_size:
                max_size = dp[i]
                max_idx = i
        
        # Reconstruct the subset using the parent pointers
        result = []
        curr = max_idx
        while curr != -1:
            result.append(nums[curr])
            curr = parent[curr]
            
        return result[::-1]
        