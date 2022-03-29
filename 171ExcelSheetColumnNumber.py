class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        i = 1
        for x in columnTitle:
            
            n += (ord(x) -64)* 26**(len(columnTitle)-i)
            i += 1
        return n