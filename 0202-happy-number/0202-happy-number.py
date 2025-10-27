class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        l=[2,3,4,5,6,8,9]
        mul=0
        while mul not in l and n!=1:
            mul=0
            while n:
                rem=n%10
                mul+=rem**2
                n=n//10
            n=mul
        return mul==1
        
        