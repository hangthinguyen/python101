# You have a list of prices of stocks, you buy a stock on a day and sell it on a different day in the future so that
# it will return the maximun value, it doesn't have profit, return 0.
# Input: prices = [7,1,5,3,6,4], Output: 5
# Input: prices = [7,6,4,3,1], Output: 0

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]

def maximum_profit(prices):

    profit = [0]

    for i in range(0, len(prices)):

        for j in range((i + 1), len(prices)):
            profit.append(prices[j] - prices[i])

    return max(profit) 
    

print(maximum_profit(prices1))
print(maximum_profit(prices2))
