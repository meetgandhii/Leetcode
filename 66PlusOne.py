class Solution:
    def plusOne(self, digits):
        s = ""
        for x in digits:
            s+=str(x)
        print(s)
        s=int(s)
        s+=1
        lst = []
        for x in str(s):
            lst.append(x)
        return lst
    
digits = [1,2,3]
res = Solution().plusOne(digits)
print(res)