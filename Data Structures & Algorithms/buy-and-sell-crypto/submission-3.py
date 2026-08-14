class Solution:
    def maxProfit(self, prices: List[int]) -> int:       
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] <= prices[r]:
                diff = prices[r] - prices[l]
                max_profit = max(max_profit, diff)
            else:
                l = r
            r = r + 1
        return max_profit
            
        
            

        