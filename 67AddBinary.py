class Solution:
    def addBinary(self, a: str, b: str) -> str:
        list1 = []
        list2 = []
        for x in a:
            list1.append(x)
        for x in b:
            list2.append(x)
        c = max(len(list1), len(list2))
        d = min(len(list1), len(list2))
        for x in range(c-d):
            if(len(list1)>len(list2)):
                list2.insert(0, '0')
            elif(len(list2)>len(list1)):
                list1.insert(0, '0')
        finallist = [0]*(len(list1))
        
        for x in range(0, len(list1)):
            list1[x] = int(list1[x])
            list2[x] = int(list2[x])
            finallist[x] = list1[x]+list2[x]
        finallist.insert(0, 0)
        for x in range(len(finallist)-1, -1, -1):
            if finallist[x]==2:
                finallist[x] = 0
                finallist[x-1] += 1
            elif finallist[x]==3:
                finallist[x]=1
                finallist[x-1]+=1
        ans = ""
        for x in finallist:
            ans+=str(x)
        ans = str(int(ans))
        return ans
    
a = "11"
b = "1"
res = Solution().addBinary(a,b)
print(res)