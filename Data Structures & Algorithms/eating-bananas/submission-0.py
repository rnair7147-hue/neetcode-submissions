class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        result = r        

        while l <= r:
            mid = l + (r-l)//2
            hours = 0
            for elem in piles:
                hours += (elem + mid - 1) // mid

            if hours <= h:
                result = mid
                r = mid - 1
            elif hours > h:
                l = mid + 1

        return result


        