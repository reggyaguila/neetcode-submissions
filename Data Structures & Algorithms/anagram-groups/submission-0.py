class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #while iterating through the list, check for length
        #while iterating, we can add it to a dictionary
        #once all strings have been added to a dictionary
        #Dictionary of dictionaries
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return list(res.values())

        