class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <=1: return False # edgecase, failout
        seen = set()
        for i in nums:
            if i not in seen: 
                seen.add(i)
            else:
                return True
        return False

# we don't need a null check, we have size 1 and nothing at the start
# this should run fast enough for a large size input 