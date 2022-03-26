class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while(start+1 < end):
            mid = start+(end-start) // 2
            if(mid*mid == x):
                return mid
            elif(mid*mid > x):
                end = mid
            elif(mid*mid < x):
                start = mid
        if end * end == x:
            return end
        return start
