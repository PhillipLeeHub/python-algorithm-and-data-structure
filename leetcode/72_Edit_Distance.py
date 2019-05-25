# 72. Edit Distance Hard
# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
def minDistance(self, word1: str, word2: str) -> int:
    # self.dict_memo = {}
    # ans = self.top_down(word1, word2)
    # return ans

    return self.bottom_up(word1, word2)


def bottom_up(self, word1: str, word2: str) -> int:
    #     r o s
    #   0 1 2 3
    # h 1 1 2 3
    # o 2 1 1 2
    # r 3 1 2 2
    # s 4 2 2 2
    # e 5 3 3 3
    # Solution matrix[5][3] = 3

    m = len(word1)
    n = len(word2)

    # Create 2D matrix with 0s
    arr = [[0] * (n + 1) for _ in range(0, m + 1)]

    # Fill in our matrix 0 => len(n)
    for i in range(0, n + 1):
        arr[0][i] = i
    # Fill in our matrix 0 => len(m)
    for i in range(0, m + 1):
        arr[i][0] = i

    # Select the min of 3 option: replace, insert, delete
    #
    # INDEX = min(replace, insert, delete)
    #  ------------------
    # | replace | insert |
    #  ------------------
    # | delete  | INDEX  |
    #  ------------------
    # [0, 1, 2, 3]
    # [1, 0, 0, 0]
    # [2, 0, 0, 0]
    # [3, 0, 0, 0]
    # [4, 0, 0, 0]
    # [5, 0, 0, 0]

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            replace = arr[j - 1][i - 1]
            insert = arr[j - 1][i]
            delete = arr[j][i - 1]

            # Check if letters match
            if word1[j - 1] == word2[i - 1]:
                # Match, no additional operation
                arr[j][i] = replace
            else:
                # Not match, add 1
                arr[j][i] = min(replace, insert, delete) + 1

    return arr[m][n]


def top_down(self, word1: str, word2: str) -> int:
    if len(word1) == 0 and len(word2) == 0:
        return 0

    if len(word1) == 0:
        return len(word2)

    if len(word2) == 0:
        return len(word1)

    if (word1, word2) in self.dict_memo:
        return self.dict_memo[(word1, word2)]

    if word1[0] == word2[0]:
        ans = self.top_down(word1[1:], word2[1:])
        self.dict_memo[(word1, word2)] = ans
        return ans
    else:
        ans = min(1 + self.top_down(word1[1:], word2[:]),
                  1 + self.top_down(word1[:], word2[1:]),
                  1 + self.top_down(word1[1:], word2[1:]))
        self.dict_memo[(word1, word2)] = ans
        return ans
