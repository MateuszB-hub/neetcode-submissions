class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = set()
        for i in range(len(nums)):          # anchor
            L, R = i + 1, len(nums) - 1
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                if total == 0: 
                    seen.add((nums[i], nums[L], nums[R])) 
                    L+=1
                    R-=1   # values, in a tuple                    # made a correction, to make [i, L, R]
                    # rather than nums[L], etc
                # == 0 → add (nums[i], nums[L], nums[R]) to seen, then move both L and R
                # total is less than 0, we need to move L up
                # <  0 → ?
                elif total < 0 : L+=1
                # total is more than 0, move R down
                elif total > 0 : R-=1
                # >  0 → ?
        return [list(t) for t in seen]