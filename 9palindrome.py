class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        temp = x
        reverse = 0
        while temp>0:
            reverse *=10
            reverse += temp%10
            temp //= 10
            # print(temp)
            # print(reverse)
        return x == reverse
#########################
##########OR#############
#########################

# # class Solution:
#     def isPalindrome(self, x: int) -> bool:
#       return str(x)==str(x)[::-1]

x = 121
res = Solution().isPalindrome(x)
print(res)