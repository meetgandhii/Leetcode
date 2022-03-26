class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ls = [0]*(n+1)
        ls[1] = 1
        ls[2] = 2
        for i in range(3, n+1):
            ls[i] = ls[i-1]+ls[i-2]
        return ls[n]

n = 6
res = Solution().climbStairs(n)
print(res)