class Solution {
    public int majorityElement(int[] nums) {
        // Return majority
        // majority element appears more than n / 2
        if (nums.length == 1) {
            return nums[0];
        }

        Map<Integer, Integer> map = new HashMap<>();

        int size = nums.length / 2;
        int majorityElement = 0;

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                map.put(nums[i], map.get(nums[i]) + 1);
                if (map.get(nums[i]) > size) {
                    majorityElement = nums[i];
                }
            } else {
                map.put(nums[i], 1);
            }   
        }

        return majorityElement;
    }
}