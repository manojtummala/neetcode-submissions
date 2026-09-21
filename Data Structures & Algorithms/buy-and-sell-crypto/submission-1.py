class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ma = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                pro = prices[r] - prices[l]
                ma = max(pro, ma)
            else:
                l = r

            r += 1
        return ma