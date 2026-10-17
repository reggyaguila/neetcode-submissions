class Solution {
    public int lengthOfLongestSubstring(String s) {

        
        Map<Character, Integer> charInd = new HashMap<>();

        int start = 0;
        int maxLen = 0;

        for (int end = 0; end < s.length(); end++) {
        // 1. Put the new index into the map. It returns the OLD index (if it existed).
        Integer prevIndex = charInd.put(s.charAt(end), end); 
        
        // 2. If prevIndex is not null, this character was seen before
        if (prevIndex != null) { 
            // 3. If the duplicate is inside our current window, shrink the window
            if (prevIndex >= start) { 
                start = prevIndex + 1; 
            }
        }
        // 4. Always calculate the maximum length of the valid window
        maxLen = Math.max((end - start + 1), maxLen);
}


        return maxLen;
    }
}
