class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #build num_set from nums
        num_set = set(nums)
        longest = 0
        for n in num_set:
        # for each n in num_set:
            if n - 1 in num_set:      # something behind me
                continue
            # I'm a start
            current = n
            length = 1
            while current + 1 in num_set:
                current +=1 # not sure if this is right, and if it's supposed to be +=1 or some value being set
                length +=1
            longest = max(longest, length) 
            # the bigger of longest and length

        return longest