class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        indexes = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in seen:
                seen[nums[i]] = i
            else:
                indexes.append(seen.get(diff))
                indexes.append(i)
                return indexes  
        return indexes