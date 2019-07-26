# 91. Decode Ways Medium
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
def numDecodings(self, s: str) -> int:
    # check empty string or null
    if not s:
        return 0

    # Use index 0 as padding
    # List up to lenght +
    dp = [0] * (len(s) + 1)

    # Only 1 way to decode an empty string
    dp[0] = 1

    # Loop through string length times
    for i in range(1, len(s) + 1):
        # Ensure digit not 0
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # check digit 10-26
        if len(s[i - 2:i]) == 2 and '10' <= s[i - 2:i] <= '26':
            dp[i] += dp[i - 2]
    # Return last index
    return dp[len(s)]
