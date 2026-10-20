class Solution {
    public int[] twoSum(int[] nums, int target) {
        //Indicies need to be unique
        //nums[i] + nums[j] == target
        //Add every number to a hashmap --> index -> nums[index]
        // [4, 5, 2]
        // {(0,4), (1,5), (1,2)} target == 7
        
        Map<Integer, Integer> map = new HashMap<>();
        int index1 = 0;
        int index2 = 0;

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                if (map.get(target - nums[i]) != i) {
                    index1 = i;
                    index2 = map.get(target - nums[i]);
                }
            }
            map.put(nums[i], i);
        }

        return new int[]{index2, index1};
    }
}
