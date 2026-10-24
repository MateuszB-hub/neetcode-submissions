class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         
        L  = 0
        R = len(numbers)-1
        total = 0
        while L<R:
            total = numbers[L]+numbers[R]
            if total == target: return [L+1, R+1]
            elif total < target: L+=1
            else:R-=1
