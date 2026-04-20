class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        desired = {}
        for i,num in enumerate(nums):
            newnum = target - num
            if newnum in desired: 
                return [desired[newnum], i]                
            else:
                desired[num] =   i
                
        return []