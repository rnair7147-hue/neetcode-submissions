class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):

            maximum = max(nums[i], maximum + nums[i])
            res = max(res, maximum)
        return res