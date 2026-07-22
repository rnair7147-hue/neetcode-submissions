class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        compl = {}

        for i,num in enumerate(nums):
            diff = target - num
            if diff in compl:
                return [compl[diff], i]
            compl[num] = i
        return []
            


