class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""
        if len(strs) == 0:
            return ans
        elif len(strs) == 1:
            return strs[0]
        m = len(min(strs, key=len))
        i = 0
        reference = strs[0]
        while i < m:        
            for myStr in strs:
                if myStr[i] != reference[i]:
                    return reference[:i]
            i += 1
        return reference[:m]


strs = ["flower","flower","flower"]
res = Solution().longestCommonPrefix(strs)
print(res)