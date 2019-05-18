# 509. Fibonacci Number easy
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).
#
#
#
# Example 1:
#
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:
#
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:
#
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
def fib(self, N: int) -> int:
    self.dict = {}
    # return self.mem_recursive(N)
    # return self.const_space_iterative(N)
    return self.dp_iterative(N)


def dp_iterative(self, N: int) -> int:
    '''
    48 ms 38
    13.2 5
    '''
    list_dp = [0, 1]
    i = 2
    while (i <= N):
        list_dp.append(list_dp[i - 1] + list_dp[i - 2])
        i += 1
    return list_dp[N]

def const_space_iterative(self, N: int) -> int:
    ''' Constant space
    NOT WORKING YET
    '''
    if N == 0:
        return 0
    if N == 1:
        return 1

    isZero = True
    index_0 = 0
    index_1 = 1
    sum = 1
    for i in range(N - 2):
        if isZero:
            index_0 = index_0 + index_1
            isZero = False
            sum += index_0
        else:
            index_1 = index_0 + index_1
            isZero = True
            sum += index_1
    return sum


def mem_recursive(self, N: int) -> int:
    '''
    36ms 79% faster
    13.3MB 5% less
    '''
    if N in self.dict:
        return self.dict[N]
    if N == 0:
        return 0
    if N == 1:
        return 1

    num1 = self.mem_recursive(N - 1)
    self.dict[N - 1] = num1
    num2 = self.mem_recursive(N - 2)
    self.dict[N - 2] = num2
    return (num1 + num2)


def recursive(self, N: int) -> int:
    # 1220ms 6.02% faster
    # 13.1MB . 5.02% less
    if N == 0:
        return 0
    if N == 1:
        return 1
    return self.fib(N - 1) + self.fib(N - 2)
