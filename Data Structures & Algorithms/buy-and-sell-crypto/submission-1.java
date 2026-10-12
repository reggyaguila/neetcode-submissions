class Solution {
    public int maxProfit(int[] prices) {
        //prices is an array of the stock price of NeetCoin on the ith day
        //choose a single day to buy one NeetCoin and choose a different day in the future to sell it
        //Return max profit you can achieve
        //Or don't make any transactions
        if (prices.length == 1) {
            return 0;
        }

        int buy = 0;
        int sell = 1;
        int profit = 0;

        while (sell < prices.length) {
            if (prices[buy] > prices[sell]) {
                buy = sell;
            } else {
                profit = Math.max((prices[sell] - prices[buy]), profit);
            }
            sell++;
        }

        return profit;
    }
}
