class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        minSpeed = r
        
        while l <= r:
            speed  = l + ((r - l)//2)
            hrs = 0
            for pile in piles:
                hrs += (pile + (speed - 1)) // speed
            
            if hrs <= h:
                minSpeed = speed
                r = speed - 1
            else :
                l = speed + 1
        return  minSpeed

        