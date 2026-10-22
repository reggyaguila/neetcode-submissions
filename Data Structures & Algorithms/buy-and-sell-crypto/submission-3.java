class Solution {
    public int maxProfit(int[] prices) {
        //[10,1,5,6,7,1]
        int globalMax = 0;
        int buy = 0;
        int sell = 0;

        while (sell < prices.length) {
            if (prices[sell] < prices[buy]) {
                buy = sell;
            }
            globalMax = Math.max(globalMax, prices[sell] - prices[buy]);
            sell++;
        }
        return globalMax;

    }
}
