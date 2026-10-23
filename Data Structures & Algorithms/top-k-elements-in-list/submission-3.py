class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for i in nums:
            counts[i]+=1
        buckets = [[] for i in range(len(nums)+1)]
        # but why make a list for every value in nums? they could all be unique? or? 
        # reminder to use two variables to grab the count and key 
        for n, c in counts.items():
            buckets[c].append(n)
            # for the count we see, add the value into the count store
        
        # now reverse iterate 
        result = list()
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result