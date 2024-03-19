class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            curr = nums[0]
            glob = nums[0]
            for i in range(1, len(nums)):
                curr = max(nums[i], curr + nums[i])
                glob = max(glob, curr)
            return glob

        max_linear = kadane(nums)
        tot = sum(nums)
        max_wrap = tot + kadane([-x for x in nums])
        return max(max_linear, max_wrap) if max_wrap != 0 else max_linear
