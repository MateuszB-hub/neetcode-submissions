class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
# step 1: count
            counts[num] +=1

        buckets = [[] for _ in range(len(nums) + 1)]   # index = count
# make the buckets needed for the length of the list, since that could all be 1 number or many different apperance counts 
        for num, count in counts.items():
# step 2: place once
            buckets[count].append(num)

        result = []
        for count in range(len(nums), 0, -1):          # highest count first
            for num in buckets[count]:
# step 3: collect, stop at k
                result.append(num)
                if len(result) == k:
                    return result
        return result