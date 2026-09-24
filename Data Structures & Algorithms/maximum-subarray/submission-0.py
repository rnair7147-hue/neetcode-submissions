class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            maxSub = max(nums[i], nums[i]+ maxSub)
            result = max(result,maxSub)
        return result
        