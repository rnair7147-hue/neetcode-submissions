class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) -1 
    
        while l <= r:
            mid = l + ((r - l) // 2)   # Overflow-safe calculation
            
            if nums[mid] == target:
                return mid
            
            # Case 1: Check if the Left portion is normally sorted
            if nums[l] <= nums[mid]:
                # Is the target inside the strict boundaries of this left sorted zone?
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left
                else:
                    l = mid + 1  # Search right
                    
            # Case 2: The Right portion must be normally sorted
            else:
                # Is the target inside the strict boundaries of this right sorted zone?
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right
                else:
                    r = mid - 1  # Search left
                    
        return -1
        