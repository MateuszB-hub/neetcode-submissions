class Solution:

    def encode(self, strs: List[str]) -> str:
        # give the string
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            # if i is at 5, and j is in range of that... 
            # put i at the number, j at the char
            # any everything in between is the string
            length = int(s[i:j])# why we do this? the number could be double, triple digit..
            #start, find word
            start = j+1
            end = start + length
            # get to the end of the word
            result.append(s[start:end])
            i = end
        return result
                
