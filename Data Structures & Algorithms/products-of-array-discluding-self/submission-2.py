class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [0 for i in range(n)]
        # make the list for L the length of the list 
        L[0] = 1 
        # we will have the list retain the values, but use the nums list
        # to get the real numbers to fill in the true prods array 
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
            # to set the current value, just get the previous value
        # we will reach the end for L
        # and then we need to do the same work for R
        R = [0 for i in range(n)]
        R[-1] = 1
        for i in range(n-2, -1, -1):
            # I need a reminder, which parameter is the one that sets the position. 
            # had to google, before I had -2, 0, -1. assuminmg, start, stop , step. 
            # google advised: n-2, -1, -1.
            # should reverse iterate 
            R[i] = R[i+1] * nums[i+1]
        # lets trace 
        """
        2, 3, 4, 5
        L[0] = 1 
        L[1] = 2
        L[2] = 2
        what does this tell me? I need to use previous num, and previous L? 
        """
        ans = [0 for i in range(n)]
        
        for i in range(n):
            ans[i] = L[i]*R[i]

        return ans