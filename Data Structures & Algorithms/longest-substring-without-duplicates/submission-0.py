class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        left = 0
        char_map = {}

        for right in range(len(s)):
            
            if s[right] in char_map:
                left = max(left, char_map.get(s[right]) + 1)
                char_map[s[right]] = right
            else:
                char_map[s[right]] = right
                
            count = max(count, right-left + 1)

        return count

            
