class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
                # print(z)
                # print(i)
                # print(len(s)-1)
            
        return z+roman[s[-1]] 
    


s= "XVI"
res = Solution().romanToInt(s)
print(res)