class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st=[]
        n=len(nums)
        res=[-1]*len(nums)
        for i in range(2*len(nums)-1,-1,-1):
            curr=nums[i%len(nums)]
            while st and st[-1]<=curr:
                st.pop()
            if i<n:
                if st:
                    res[i]=st[-1]
            st.append(curr)
        return res

        