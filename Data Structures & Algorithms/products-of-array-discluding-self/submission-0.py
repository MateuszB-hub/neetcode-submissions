class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # so the left loop doesn't start at 0, 0 is set at 1 
        left = [0 for i in range(len(nums))]
        left[0] = 1 
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            # so we take the existing value of 
            # 1 and then multiply by the actual value of the index 
            # and we do so with every value going forward
            # 2, 3, 4, 5
            # index 1 would be 1 x 2
            # then index 3 would be...  2 x 3 to make 6
            # and then index 4 is 6 x 4 to make 24
            # now let's do this for right
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
        """
        for each i , multiply every other number, that's O(n^2). 
        reframe
        everything except i, everything to the lext of i and everything to the right of i
        that's the trick 

        what do i need to remember about the numbers I've already passed?
        the running product. wasn't sure what was meant by the cue question, could be a simpler way to explain it
        unless cue meant like , cue the scene, but that sounds more like queue the scene. 

        walk left to right, and the running product at each index is everything to the left
        everything to the right isn't available 
        and this is where I get confused trying to retain and make sense of both left and right stuff. 
        like I can get the running product from the left.

        everything to the right is something not being considered... so a backwards pass is made once
        we get the left products, we then get the right products going in reverse...?

        [2,3,4,5]

        we start at 0, that's default 1, move to  3, get 3, move to 4, get 12, move to 5, get 60
        then going back index 3 gets 1, index 2 gets 4, index 2, gets 12, index 1 gets 24
        then the final end 
        I think somehow I got the values backwards, where index 1 is 60, but I have 24

        2, 3, 4, 5,
        2, 6, 24, 120
        120, 60, 20, 5
        but what I see is that in index 3, isn't not 5, but 1? 

        so when we are at index 0
        nothing is to the left of it 
        at index 1, we only have 2 from index 0 that is the real value 
        at index 2, we have 2 and 3 to the left, giving the third index 6, and then the final index gets all values to the left of it
        being 2, 3, 4. making 24 


        now from the right 

        5 is 1
        4 is 5
        3 is 20
        2 is 60 

        """