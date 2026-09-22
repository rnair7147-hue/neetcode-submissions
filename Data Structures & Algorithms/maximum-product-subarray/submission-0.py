class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minP = nums[0]
        maxP = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0:
                minP, maxP = maxP, minP

            minP = min(num, num * minP)
            maxP = max(num, num * maxP)

            result = max(result, maxP)

        return result