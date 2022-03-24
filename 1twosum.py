class Solution:
    def twoSum(self, nums, target):
        result = []
        index_map = {}
        for i, n in enumerate(nums):
            # Difference which needs to be checked
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        result.sort()
        return result

nums = [2,3,5,7]
target = 9
res = Solution().twoSum(nums, target)
print(res)

