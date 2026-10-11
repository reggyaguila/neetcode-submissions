class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        int counts1[] = new int[26];
        int counts2[] = new int[26];

        for (int i = 0; i < s.length(); i++) {
            counts1[s.charAt(i) - 'a']++;
            counts2[t.charAt(i) - 'a']++;
        }


        return Arrays.equals(counts1,counts2);

    }
}
