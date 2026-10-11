class Solution {
    public boolean hasDuplicate(int[] nums) {
        //Compare the length of a hashset vs an array
        Set<Integer> unique = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (!unique.add(nums[i])) {
                return true;
            }
        }

        return false;
    }
}