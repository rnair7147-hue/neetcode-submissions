class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maximum , minimum = nums[0], nums[0]
        result = nums[0]

        for i in range(1,len(nums)):

            if nums[i] < 0:
                maximum , minimum = minimum , maximum

            maximum = max(nums[i], maximum * nums[i])
            minimum = min(nums[i], minimum * nums[i])

            result = max(result, maximum)
        
        return result

        