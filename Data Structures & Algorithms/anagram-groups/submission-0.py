class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we want to get a dict that returns key value of anagram'd words 
        # so what we have to have is a word sort that sorts each of the words which makes it easy to collect them
        # and using the sorted word as a key, and unsorted saved to the list 
        res = defaultdict(list)
        # hiccup 1: needed to add (list)
        # good news, changed dict to defaultdict on my own since I didn't want to handle default value setting
        for word in strs:
            sortedWord = "".join(sorted(word))

            res[sortedWord].append(word)
        return list(res.values())
        # hiccup 2: needed to put list in
        # could have also probably done [res.values()], but this wasn't tested and is an assumption