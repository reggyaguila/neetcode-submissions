class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Need global max
        #window_length - max_frequency <= k
        #invalid : window_length - max_frequency > k --> shift the left pointer
            #Decrement the value of the character's frequency in the hash map

        global_max = 0
        left, right = 0, 0
        char_frequency = {}
        max_freq = 0

        while (right < len(s)):
            window_length = right - left + 1
            
            char_frequency[s[right]] = char_frequency.get(s[right], 0) + 1

            max_freq = max(max_freq, char_frequency[s[right]])

            if window_length - max_freq <= k:
                global_max = max(window_length, global_max)
            else:
                char_frequency[s[left]] -= 1
                left += 1
                
            

            right += 1
        
        return global_max



        