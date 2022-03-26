class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1 = []
        s = s.strip()
        s += " "
        word = ""
        for x in s:
            word+=x
            if(x == " "):
                word = word.strip()
                list1.append(word)
                word = ""
        return len(list1[-1])
    
s = "Fly me to the moon "
res = Solution().lengthOfLastWord(s)
print(res)