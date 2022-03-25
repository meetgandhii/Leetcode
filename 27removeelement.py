class Solution:
    def removeElement(self, nums, val):
        a = []
        count = 0
        for i in nums:
            if i!=val:
                a.append(i)
            else:
                count += 1
        a.sort()
        for x in range(0, len(a)):
            nums[x]=a[x]
        return len(nums)-count
    
nums = [0,1,2,2,3,0,4,2] 
val = 2
res = Solution().removeElement(nums, val)
print(f"{res}, nums = {nums[:res]}")