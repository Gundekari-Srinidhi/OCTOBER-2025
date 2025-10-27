class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        l=set()
        mul=0
        while n!=1 and n not in l:
            l.add(n)
            mul=0
            while n:
                rem=n%10
                mul+=rem**2
                n=n//10
            n=mul
        return mul==1
        
        