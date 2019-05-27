# 415. Add Strings Easy
#
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
def addStrings(self, num1: str, num2: str) -> str:
    return self.init_code(num1, num2)
    # return self.add_string_zip(num1, num2)

def init_code(self, num1: str, num2: str) -> str:
    '''
    Runtime: 72 ms, faster than 20.72% of Python3 online submissions for Add Strings.
    Memory Usage: 13.3 MB, less than 38.61% of Python3 online submissions for Add Strings.
    '''
    sum_string = ''
    carry = 0
    i = len(num1)
    j = len(num2)
    while (i > 0 or j > 0):
        digit1 = '0' if i <= 0 else num1[i - 1]
        digit2 = '0' if j <= 0 else num2[j - 1]

        int_1 = ord(digit1) - ord('0')
        int_2 = ord(digit2) - ord('0')
        curr_sum = int_1 + int_2 + carry
        carry = curr_sum // 10
        sum_string = str(curr_sum % 10) + sum_string

        i -= 1
        j -= 1
    if carry:
        sum_string = '1' + sum_string
    return sum_string

def add_string_zip(self, num1: str, num2: str) -> str:
    '''
    Runtime: 52 ms, faster than 74.83% of Python3 online submissions for Add Strings.
    Memory Usage: 13.4 MB, less than 19.13% of Python3 online submissions for Add Strings.
    '''
    from itertools import zip_longest
    result = ''
    carry = 0

    for digit1, digit2 in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
        int_1 = ord(digit1) - ord('0')
        int_2 = ord(digit2) - ord('0')

        curr_sum = int_1 + int_2 + carry
        result = str(curr_sum % 10) + result
        carry = curr_sum // 10

    return '1' + result if carry == True else result


