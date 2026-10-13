class Solution {
    public int search(int[] nums, int target) {
        //[-1,  0,2,  4,6,8]
        //Even lenghts length % 2 == 0
        //Odd lengths
        if (nums.length == 1) {
            if (nums[0] == target) {
                return 0;
            } else{
                return -1;
            }
        }

        int start = 0;
        int end = nums.length - 1; //5
        

        while (start <= end) { 
            int mid = start + (end - start) / 2; //4

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                end = mid - 1;
            } else {
                start = mid + 1; //Start = 3
            }
        }

        return -1;
    }
}
