class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []        
        sorted_list = sorted(nums)
        newItem = []
        for i,num in enumerate(sorted_list):
            target = -num
            left = i + 1
            right = len(sorted_list) - 1
            while (left < right):
                if sorted_list[left] + sorted_list[right] == target:
                    newItem = sorted([num,sorted_list[left],sorted_list[right]])
                    if newItem not in result:
                        result.append(newItem)
                    left += 1
                    right -= 1
                elif sorted_list[left] + sorted_list[right] > target:
                    right -= 1
                else:
                    left += 1
                    
        return result     


            
