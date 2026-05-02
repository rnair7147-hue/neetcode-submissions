class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        desired = {}
        for i,num in enumerate(nums):
            difference = target - num
            if  difference in desired:
                break
                #desired[difference] = i
            else:
                desired[num] = i
        return [desired.get(difference), i]
    


