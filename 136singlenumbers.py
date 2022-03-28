class Solution:
    def singleNumber(self, nums):
        print(nums)
        numsdup = list(set(nums))
        nums1 = nums[:]
        for x in numsdup:
            nums1.remove(x)
            
        for x in nums1:
            nums.remove(x)
            nums.remove(x)
            
            
        return nums[0]
        