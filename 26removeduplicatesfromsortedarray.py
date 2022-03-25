class Solution:
    def removeDuplicates(self, nums):
        a = list(set(nums))
        a.sort()
        for i in range(0, len(a)):
            nums[i]=a[i]
        return len(a)
    
    
nums = [1,1,2]
res = Solution().removeDuplicates(nums)
print(f"{res}, nums = {nums[:res]}")