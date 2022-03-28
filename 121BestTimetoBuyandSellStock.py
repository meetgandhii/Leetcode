# def isgreat(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# class Solution:
#     def maxProfit(self, prices):
#         min_val = min(prices)
#         index = prices.index(min_val)
#         max_val = max(prices[index:])
#         return max_val-min_val


# def isgreat(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# class Solution:
#     def maxProfit(self, prices):
#         z = 0
#         max_val = 0
#         for i in range(0, len(prices)):
#             max_val = max(prices[i+1:], default=0)
#             z = isgreat(z, max_val-prices[i])
#         return z


# prices = [1,2,3,4,5,6,7]
# print(prices[:3])

# def isgreat(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# class Solution:
#     def maxProfit(self, prices):
#         if(len(prices)==1):
#             return 0
#         min_val = min(prices, default=0)
#         index = prices.index(min_val)
#         max_val = max(prices[index:])
        
#         print(f"max: {max_val}, min: {min_val}")
#         x = max_val-min_val
        
#         max_val1 = max(prices)
#         index1 = prices.index(max_val1)
#         min_val1 = min(prices[:index1], default=prices[0])
#         print(f"max: {max_val1}, min: {min_val1}")
#         x1 = max_val1-min_val1
#         return isgreat(x,x1)

# list2 = []
# for i in range(0, len(list1)-1):
#     if(list1[i]-list1[i+1]) == 3:
#         print(list1[i])
        

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n<2:
            return 0
        maxprof = 0
        mincost = prices[0]
        for x in prices:
            maxprof = max(maxprof, x-mincost)
            mincost = min(mincost, x)
        return maxprof