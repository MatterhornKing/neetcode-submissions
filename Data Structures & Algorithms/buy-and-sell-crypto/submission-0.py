class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        max_pro = 0
        min_s = prices[0]
        while i < len(prices):
            
            pro = prices[i] - min_s
            if pro > max_pro:
                max_pro = pro
            if prices[i] < min_s:
                min_s = prices[i]
            i += 1
        return max_pro
            
