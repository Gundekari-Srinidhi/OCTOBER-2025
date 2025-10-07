class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=list(set(nums1))
        b=list(set(nums2))
        l=[]
        for i in a:
            if i in b:
                l.append(i)
        return l
        