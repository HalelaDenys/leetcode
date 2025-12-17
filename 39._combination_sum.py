class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def backtrack(start, current, target):
            if target == 0:
                result.append(current[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, target - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result


candidates = [2,3,6,7]
target = 7
sol = Solution()
print(sol.combinationSum(candidates, target))