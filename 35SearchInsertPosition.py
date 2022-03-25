class Solution:
    def searchInsert(self, nums, target):
        nums.append(target)
        nums = list(set(nums))
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return i



nums = [3,6,8]
target = 0
res = Solution().searchInsert(nums, target)
print(res)