class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i,num in enumerate(nums):
            if i == 0:
                prefix[i] = 1
            else:
                prefix[i] = prefix[i-1]* nums[i -1]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix[j] = 1
            else:
                suffix[j] = suffix[j + 1] * nums[j +1]
        
        product_array = [1] * len(nums)
        
        for i in range(len(nums)):
            product_array[i] = prefix[i] * suffix[i]
        
        return product_array

    