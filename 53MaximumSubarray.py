# BruteForce
# def isgreater(x, y):
#     if x>y:
#         return x
#     else:
#         return y
# def listsum(x):
#     y=0
#     for i in x:
#         y+=i
#     return y
# class Solution:
#     def maxSubArray(self, nums):
#         if len(nums)==1:
#             return nums[0]
#         x=0
#         for i in nums:
#             x+=i
        
#         for i in range(0, len(nums)):
#             for j in range(0, len(nums)+1):
#                 if(i!=j and j>i):
#                     x=isgreater(x, listsum(nums[i:j]))                
#         return x
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        max_ending_here = 0

        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0  
        return max_so_far
    
    
    
nums = [1,2,3,4,5,-5]
res = Solution().maxSubArray(nums)
print(res)