class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i need to set two pointers
        # go from both ends to the middle
        # skip over special chars, and whitespaces
        # and lower any alphas 
        if len(s) <=1 :
            return True

        L = 0
        R = len(s)-1
        # had to make these counts since I was looking at the characters,
        # and not the counts which in turn would make l and r both having 't' fail. 
        while L<R:
            print("L", s[L])
            print("R", s[R])
            if s[L].isalnum() == False or s[L] == " ":
                L +=1
                continue
            if s[R].isalnum() == False or s[R] == " ":
                R -=1
                continue
            
            if s[L].lower()!=s[R].lower():
                return False
            L+=1
            R-=1
            # my issue here is that r progresses when l needs to go first? 
            # like for s="No lemon, no melon"
            # L get's No, R get's on
            # but then how do I handle L getting to the space and R moving on? 
            # just move where the iteration happens? 
            # or flip how i do the iteraiton, where i only iterate on failure (doing that now). 
            # if we find that L hit's it's value, we need to move it twice? +2? no ,that breaks the code. 
            # i solve this before but i can't remember the specific fix to the break. 

        print("end")
        return True
                