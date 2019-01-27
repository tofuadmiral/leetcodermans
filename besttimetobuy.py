class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        big=0
        for i in range(n):
            for j in range(n):
                if i<j and prices[i]<prices[j]:
                    if prices[j]-prices[i]>big:
                        big=prices[j]-prices[i]
        return big