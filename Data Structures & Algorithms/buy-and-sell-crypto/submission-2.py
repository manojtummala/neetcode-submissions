class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        mi = prices[0]


        for i in prices:
            ma = max(ma, i - mi)
            mi = min(mi, i)

        return ma