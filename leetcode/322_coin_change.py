# 322. Coin Change Medium
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Note:
# You may assume that you have an infinite number of each kind of coin.
def coinChange(self, coins: List[int], amount: int) -> int:
    '''
    Runtime: 1356 ms, faster than 55.61% of Python3 online submissions for Coin Change.
    Memory Usage: 13.7 MB, less than 24.25% of Python3 online submissions for Coin Change.
    '''
    # Initialize the list to amount + 1
    ans_list = [(amount + 1)] * (amount + 1)

    # Set 0 amount to require 0 coins
    ans_list[0] = 0

    # Start with 1 amount
    curr_amount = 1
    # curr_amount = 0 1 2 3 4 5 6 7 8 9 10 11
    #               0 1 1 2 2 1

    # Loop through all amount
    while (curr_amount < amount + 1):
        # Try each coin
        for coin in coins:
            # Check coin is less then amount
            if coin <= curr_amount:
                # Coin can be used, calculate remainding amount
                remainder = curr_amount - coin

                # Get the minimum coin used previously calculated vs current coin
                ans_list[curr_amount] = min(ans_list[remainder] + 1, ans_list[curr_amount])
        # Move to next amount
        curr_amount += 1
    # if amount has not change, no coins were used
    if ans_list[amount] == amount + 1:
        return -1

    # Return the bottom up result
    return (ans_list[amount])