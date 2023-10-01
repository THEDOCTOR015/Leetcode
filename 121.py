"""
Answer:
"""
class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices :
            if sell > buy and sell - buy > profit:
                profit = sell - buy
            elif sell < buy:
                buy = sell
        return profit
"""
Tests:
"""
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4])==5)
print(solution.maxProfit([7,6,4,3,1])==0)
print(solution.maxProfit([1,2])==1)