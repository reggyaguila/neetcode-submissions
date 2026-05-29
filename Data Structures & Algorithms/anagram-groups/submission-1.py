class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #In a dictionary, you access a missing key
        #W/ defaultdict, we give any non-existing accessed key a default value
        res = defaultdict(list)

        #We're looping through strings list
        for s in strs:
            #Setting up a list of 0's to count chars a..z in a str
            count = [0] * 26
            #Loop through a given str
            for c in s:
                #Sub ASCII, get index for count list
                count[ord(c) - ord('a')] += 1
            
            #Finds key associated with that specific str char frequency and adds to list
            res[tuple(count)].append(s)

        return list(res.values())
        