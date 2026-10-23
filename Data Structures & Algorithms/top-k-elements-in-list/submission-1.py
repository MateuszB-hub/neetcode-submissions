class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # capture counts of numbers
        counts = defaultdict(int)
        for i in nums:
            counts[i] +=1
        # save the counts to keys,and numbers to value list 
        buckets = [[] for i in range(len(nums)+1)]
        # make a list for each and + 1 to account for index 0 
        for num, count in counts.items():
            buckets[count].append(num)
            # save the number to the count
        
        result = [] 
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
        # iterate from end to front 