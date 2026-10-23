class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # so the left loop doesn't start at 0, 0 is set at 1 
        left = [0 for i in range(len(nums))]
        left[0] = 1 
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        right = [0 for i in range(len(nums))]

        right[-1] = 1 
        for i in range(len(nums)-2, -1, -1):
            # had to internet search the for loop range method
            right[i] = right[i+1] * nums[i+1]
        
        #then at the end multiply them together to get the final output 
        total = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            total[i] = left[i] * right[i]
        return total