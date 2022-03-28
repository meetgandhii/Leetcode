class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for x in s:
            if (x.isalnum() and x!= " "):
                s1 += x
        if s1 == "":
            return True
        print(s1)
        if s1.lower() == s1[::-1].lower():
            return True
        else:
            return False
        