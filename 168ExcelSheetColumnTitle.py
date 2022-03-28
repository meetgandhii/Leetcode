class Solution:
    def convertToTitle(self, columnNumber):
        ch = ""
        while(columnNumber>0):
            if(columnNumber%26==0):
                ch+="Z"
                columnNumber//=26
                columnNumber -=1
            else:
                ch+=chr((columnNumber%26)+64)
                columnNumber//=26
                
        return ch[::-1]

columnNumber = 701
res = Solution().convertToTitle(columnNumber)
print(res)