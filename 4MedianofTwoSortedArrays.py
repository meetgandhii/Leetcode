class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fin = []
        for i in nums1:
            fin.append(i)
        for i in nums2:
            fin.append(i)
        fin.sort()
        a = len(fin)
       
        if (a%2==0):
            
            ans = (fin[(a//2)-1]+fin[a//2])/2
        else:
            ans = fin[a//2]
        return ans