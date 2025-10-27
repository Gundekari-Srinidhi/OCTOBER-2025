class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        s=[[0]*n for i in range(n)]
        sr=0
        sc=0
        er=n-1
        ec=n-1
        num=1
        while sr<=er and sc<=ec:
            for i in range(sc, ec+1):
                s[sr][i]=num
                num+=1
            sr+=1
            for i in range(sr, er+1):
                s[i][ec]=num
                num+=1
            ec-=1
            if sr<=er:
                for i in range(ec,sc-1,-1):
                    s[er][i]=num
                    num+=1
                er-=1
            if sc<=ec:
                for i in range(er,sr-1,-1):
                    s[i][sc]=num
                    num+=1
                sc+=1
        return s

        