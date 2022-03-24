class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        if (s[0]==")"or s[0]=="}"or s[0]=="]"):
            return False
        list1 = []
        def canpop(x, l: list1):
            if len(l)==0:
                l.append("1")
            
            elif l[-1]==x:
                try:
                    l.pop(-1)
                except:
                    l.append("1")
            else:
                l.append("1")
        
        for i in s:
            if(i=="(" or i=="{" or i=="["):
                list1.append(i)
            elif i==")":
                canpop("(", list1)
            elif i=="]":
                canpop("[", list1)
            elif i=="}":
                canpop("{", list1)
        if(len(list1)!=0):
            return False
        if "1" in list1:
            return False
        else:
            return True


s = "(){}[]"
res = Solution().isValid(s)
print(res)