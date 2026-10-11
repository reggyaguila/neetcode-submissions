class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsMap = new HashMap<>();

        //Loop through the array, for each element, we are going to subtract it from target
        //Check if that number exists in the HashMap

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (numsMap.containsKey(complement)) {
                return new int[]{numsMap.get(complement), i};
            }

            numsMap.put(nums[i], i);
        }
        return new int[]{-1,-1};
    }
}
