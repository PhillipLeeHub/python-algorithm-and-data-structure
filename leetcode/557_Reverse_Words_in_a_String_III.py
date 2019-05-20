# 557. Reverse Words in a String III easy
#
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.
def reverseWords(self, s: str) -> str:
    res = ''
    splited = s.split(' ')

    for i, word in enumerate(splited):
        res += ''.join(reversed(word))
        if i != len(splited) - 1:
            res += ' '

    return res

