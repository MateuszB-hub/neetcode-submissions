class Solution:

    def encode(self, strs: List[str]) -> str:
        # find the length of the string, and append '#' 
        # and save all list strings into one big strings with the prefix length 
        res = ""
        for i in strs:
            length = len(i)
            res += str(length) + '#' + i
        
        print(res)
        return res
        # completed encode
        # ["Hello","World"]
        # output: 5#Hello5#World
    def decode(self, s: str) -> List[str]:
        # to decode, capture the length of the number, so if the number is xx, or xxx 
        # need to find the '#' which would be j
        i = 0
        res = []
        while i < len(s):
            j = i
            print("i", i)
            print("j", j)
            while s[j] != '#':
                print("i finding #", i)
                print("j finding #", j)
                print("s[j]", s[j])
                j+=1                                 
                print("s[j]", s[j])
            length = s[i:j]
            length = int(length)
            word = s[j+1 : j+1+int(length)]
            i = j+1+int(length)
            res.append(word)
        return res

