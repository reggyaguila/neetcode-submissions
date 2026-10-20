class Solution {
    public int maxProfit(int[] prices) {
        //Two pointers
        //First pointer is our starting pointer (cheapest purchase day)
        //Second pointer is our searching pointer (looking for the next cheapest purchase day)

        int globalMax = 0;

        int start = 0;
        int search = 0;

        while (search < prices.length) {

            if (prices[start] < prices[search]) {
                int currentMax = prices[search] - prices[start];
                globalMax = Math.max(globalMax, currentMax);
            } else {
                start = search;
            }

            search++;
        }

        return globalMax;
    }
}
