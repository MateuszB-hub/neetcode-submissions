class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# add one from s and then subtract with t
# by the end if we end up with 0, we save on a hashmap and then
# we can know easier if an anagram exists by a 0 total count, no leftovers
        if len(s) != len(t): return False
        # this covers us for the for loop later

        # choosing 1 map since it saves a little and can be
        # easily understood by chars or comments in code
        result = defaultdict(int)
        # we have the map, add s, subract t
        # but what if s and t are not the same and t subtracts? 
        # that's fine, have t make -1 from dict.get(0 -1) or something like that 
        # to get a default value 0 and then take 1 away 
        for i in range (len(s)):
            result[s[i]] +=1
            result[t[i]] -=1
            # i forgot how to set the default and googled the reminder
            # the only edits i had to do was the range finding
            # and remind myself of using i in t and s
            #and I changed dict to defaultdict for automated default value setting
            # and a new method called all(), never used that kind of return respponse. so this solutino isn't that original

        return all(count == 0 for count in result.values())