//The answer of leetcode top 1nterview 150 the question number 121 (best time to buy and sell stock) written by Kasra Namiranian.
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let max_profit = 0;
    let buy_price = prices[0];
    for (let day=1; day<prices.length; day++){
        if(buy_price > prices[day]){
            buy_price = prices[day];
        } else if (max_profit < prices[day] - buy_price) {
            max_profit = prices[day] - buy_price;
        }

    }return max_profit;
};
