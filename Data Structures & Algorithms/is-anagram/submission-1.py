class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if the lists are equal length
        if len(s) != len(t):
            return False
        
        #create a dictionary, we'll compare if the the two dicts are equal
        ana_dict1 = {}
        ana_dict2 = {}

        for i in range(len(s)):
            ana_dict1[s[i]] = ana_dict1.get(s[i], 0) + 1
            ana_dict2[t[i]] = ana_dict2.get(t[i], 0) + 1

        return ana_dict1 == ana_dict2