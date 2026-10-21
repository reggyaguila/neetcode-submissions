class Solution {
    public String frequencySort(String s) {
        //Define the HashMap for freq counting
        HashMap<Character, Integer> map = new HashMap<>();
        //Get character frequencies
        for (char ch : s.toCharArray()) {
            map.merge(ch, 1, Integer::sum);
        }
        //Now we need to sort these frequencies
        List<Map.Entry<Character, Integer>> listCounts = new ArrayList<>(map.entrySet());
        
        listCounts.sort((a,b) -> b.getValue().compareTo(a.getValue()));

        //Need to create a new string
        StringBuilder newS = new StringBuilder();

        for (int i = 0; i < listCounts.size(); i++) {
            Map.Entry<Character, Integer> e = listCounts.get(i);
            for (int j = 0; j < e.getValue(); j++) {
                newS.append(e.getKey());
            }
        }

        return newS.toString();
    }
}