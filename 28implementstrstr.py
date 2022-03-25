class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (haystack == "" and haystack!=needle):
            return -1
        elif (needle == "" or haystack[0] == needle or haystack == needle):
            return 0
        a = len(haystack)
        b = len(needle)
        j=0
        for i in range(b, a+1):
            if haystack[j:i] == needle:
                return j
            j+=1
        return -1    
        
haystack = "hello"
needle = "ll"
res = Solution().strStr(haystack, needle)
print(res)
