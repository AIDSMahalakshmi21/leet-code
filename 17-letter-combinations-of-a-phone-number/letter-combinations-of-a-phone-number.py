class Solution:

    def letterCombinations(self, digits):
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = [""]
        for digit in digits:
            res = [prev + letter for prev in res for letter in mapping[digit]]

        return res