class Solution(object):
    def longestPalindrome(self, s):
        res = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        for i in range(len(s)):
            palindrome_odd = expand(i, i)
            palindrome_even = expand(i, i + 1)

            if len(palindrome_odd) > len(res):
                res = palindrome_odd
            if len(palindrome_even) > len(res):
                res = palindrome_even

        return res