class Solution:
    def generate(self, numRows):
        list1 = [[1],[1,1]]
        list2 = []
        if numRows == 0:
            return [[]]
        elif numRows==1:
            return [[1]]
        elif numRows == 2:
            return list1
        for x in range(3, numRows+1):
            list2 = [0]*x
            list2[0]=1
            list2[x-1]=1
            for y in range(1, x-1):
                list2[y]=list1[x-2][y]+list1[x-2][y-1]

            list1.append(list2)
        return list1
    
numRows = 5
res = Solution().generate(numRows)
print(res)