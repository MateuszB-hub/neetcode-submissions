class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need return the pair where target and counter is 
        # the indexes of those values that get to target 
        res = [] 
        # we will want to insert the values into res 
        # iterate through the list and have the index taken
        # I could enumerate as I want the position and value 
        seen = dict()
        for ind, val in enumerate(nums):
            complement = target - val
            if complement in seen: 
                # a number can't use itself? like 5 is using 5? or I just change the ordering of activities
                res = [seen[complement], ind]
                # get the current number and then the other number 
                return res
            seen[val] = ind
            # moving this down here from lines 12/13 fixed my issue 
            # but now there are dupe values... 
        return []