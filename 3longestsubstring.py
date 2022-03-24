class Solution:
    def lengthOfLongestSubstring(self,s):
        check = []
        checklist = []
        for x in range(len(s)):
            if s[x] not in check:
                check.append(s[x])
            else:
                # print(check)
                checklist.append(check[:])
                # print(checklist)
                m = check.index(s[x])+1
                for i in range(m): #check position of the alphabet previously occurred...pop everything till there
                    # print(len(check))
                    # print(check)
                    check.pop(0)
                    # print(check)
                check.append(s[x])
        checklist.append(check)
        checklist.sort(key=len)
        return len(checklist[-1])
        # return checklist

s = "pwpwkew"
res = Solution().lengthOfLongestSubstring(s)
print(res)

