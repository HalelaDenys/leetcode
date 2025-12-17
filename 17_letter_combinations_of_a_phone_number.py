class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) <= 0:
            return []

        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = []

        def backtrack(idx = 0, path = ""):
            if idx == len(digits):
                result.append(path)
                return

            for latter in phone_map[digits[idx]]:
                backtrack(idx + 1, path + latter)

        backtrack()
        return result
