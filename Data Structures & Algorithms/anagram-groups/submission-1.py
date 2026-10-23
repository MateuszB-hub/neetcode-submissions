class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res= defaultdict(list)
        for wrd in strs: 
            sortedWord = "".join(sorted(wrd))
            res[sortedWord].append(wrd)
        
        return list(res.values())