class Solution {
    Map<String, List<String>> anagramMap = new HashMap<>();
    public List<List<String>> groupAnagrams(String[] strs) {

        
        for (int i = 0; i < strs.length; i++) {
            int[] counts = new int[26];
            for (int j = 0; j < strs[i].length(); j++) {
                counts[strs[i].charAt(j) - 'a'] += 1;
            }

            String key = Arrays.toString(counts);
            addToMap(key, strs[i]);
        }

        List<List<String>> listOfString = new ArrayList<>();
        for (Map.Entry<String, List<String>> entry : anagramMap.entrySet()) {
            List<String> inner1 = entry.getValue();
            listOfString.add(inner1);
        }

        return listOfString;
        

    }

    public void addToMap(String key, String str) {
        List<String> string = anagramMap.computeIfAbsent(key, k -> new ArrayList<>());
        string.add(str);
    }
}
