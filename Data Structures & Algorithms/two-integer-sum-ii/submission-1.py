class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i,num in enumerate(numbers):
            if target - num in numbers:
                return [i + 1,numbers.index(target - num) + 1]
        return []
        

        