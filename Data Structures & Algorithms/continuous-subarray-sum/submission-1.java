class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        seen.put(0, -1);

        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];

            int remainder = sum % k;

            if (seen.containsKey(remainder)) {
                int previousIndex = seen.get(remainder);

                if (i - previousIndex >= 2) {
                    return true;
                }
            } else {
                seen.put(remainder, i);
            }
        }

        return false;
    }
}