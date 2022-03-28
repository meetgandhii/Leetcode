class Solution:
    def majorityElement(self, nums):
        n = len(nums)//2 +1
        count=0
        numss = list(set(nums))
        for i in numss:
            for j in nums:
                if i==j:
                    count+=1
                if n == count:
                    return i
                